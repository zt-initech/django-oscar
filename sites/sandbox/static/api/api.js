// Custom subclasses of basecamp classes to work with Tastypie
// See http://paltman.com/2012/04/30/integration-backbonejs-tastypie/
window.TastypieModel = Backbone.Model.extend({
    baseUrl: function() {
      var tempUrl = Backbone.Model.prototype.url.call(this);
      return (tempUrl.charAt(tempUrl.length - 1) == '/' ? tempUrl : tempUrl+'/');
    },
    url: function() {
      return this.baseUrl();
    }
});
window.TastypieCollection = Backbone.Collection.extend({
    parse: function(response) {
        this.recent_meta = response.meta || {};
        return response.objects || response;
    }
});

// Backbone models
// ===============

var Product = TastypieModel.extend({
    urlRoot: '/api/products/'
}, {
    fetchById: function(id) {
        var obj = new Product({'id': id});
        obj.fetch();
        return obj;
    }
});

var Products = TastypieCollection.extend({
    url: '/api/products/',
    model: Product,
    startsWith: function() {
        return this.filter(function(p) {
            return p.get('title') == 'The Debutante';
        });
    }
}, {
    fetchAll: function() {
        var products = new Products();
        products.fetch();
        return products;
    },
    fetchByQuery: function() {
        var products = new Products();
        products.fetch({data: {'title': 'The Debutante'}});
        return products;
    }
});

// Knockout view models
// ====================

// "view model" for Knockout
function ProductList() {
    var self = this;

    // Methods

    self.filterProducts = function() {
        // Note we simply modify the current collection in place, we don't instantiate a new one.
        // We use the .collection method to load a new dataset into the obserable
        // See http://kmalakoff.github.com/knockback/doc/index.html
        backboneData.products.fetch({data: {'title__icontains': self.query()}});
        self.products.collection(backboneData.products);
    };
    self.resetFilters = function() {
        backboneData.products.fetch();
        self.products.collection(backboneData.products);
    };

    // Data - keep a reference to the backbone collections
    var backboneData = {
        'products': Products.fetchAll()
    };
    self.products = kb.collectionObservable(backboneData.products);

    // No initial filter
    self.query = ko.observable();
}


function test_backbone() {
    console.log("Testing Backbone");

    console.log("Loading products");
    var products = new Products();
    products.fetch();
    console.log(products);

    console.log("Loading a single product");
    var product = new Product({'id': 100});
    product.fetch();
    console.log(product);

    console.log("Loading a single product using classmethod");
    p2 = Product.fetchById(4);
    console.log(p2);

    console.log("Saving ");
    p = new Product({'title': 'Testing'});
    p.save();
}

function test_knockout() {
    console.log("Knockout!");
    ko.applyBindings(new ProductList());
}

$(function(){
    // test_backbone();
    test_knockout();
});
