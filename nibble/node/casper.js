var casper = require('casper').create();
casper.userAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X)');
var url = 'http://www.spicesthaicafesd.com/#!starters/c1n4n';


// casper.start(url, function() {
//     require('utils').dump(this.getElementsAttribute('span')); // "Google"
// });

// casper.run();
casper.start(url, function() {
    var js = this.evaluate(function() {
		return document;
	});
  var listText = this.getElementsInfo('span')
            ,i=0
            ,l=listText.length
            ;
  var paraText = this.getElementsInfo('p')
            ,p=paraText.length
            ;
  // console.log("LIST VALUES");
  // for (; i<l; i++){
  //     console.log(listText[i].text);
  // }
  console.log("PARA VALUES");
  for (i=0; i<p; i++){
      console.log(paraText[i].text);
  }
});
casper.run();
