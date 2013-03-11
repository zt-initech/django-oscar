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

//

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


function test() {
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
    var p2 = Product.fetchById(4);
    console.log(p2)

    console.log("Saving ");
    p = new Product({'title': 'Testing'});
    p.save();
}

$(function(){ test(); });
