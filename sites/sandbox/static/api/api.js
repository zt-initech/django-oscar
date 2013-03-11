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
    model: Product
});

// Knockout view models

// "view model" for Knockout
function ProductList() {
    var self = this;

    // Methods

    // Fetch products using Backbone
    self.getProducts = function() {
        var products = new Products();
        products.fetch();
        return products;
    };

    // Data
    var products = self.getProducts();
    self.products = kb.collectionObservable(products);
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
