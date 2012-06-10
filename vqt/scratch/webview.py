import sys
from PyQt4 import QtGui, QtCore, QtWebKit

r = ''
for i in xrange(1000):
    r += 'This is some <reg class="b%d" onclick="woot(this);">b%d</reg>text<br>' % (i%100, i%100)

htmldoc = '''
<html>

Hi mom!

<style title="woowoo" type="text/css">
body {
    color: #00ff00;
    background-color: #000000;
}

div.foobar {
    color: #0000ff;
    background-color: #000000;
}

reg.edx {
    color: #0000ff;
    background-color: #000000;
}

</style>

<script language="javascript">

function colorCssClass(seltext, color, bgcolor) {

    var i = 0;
    //alert(document.styleSheets[0].title);
    var myrules = document.styleSheets[0].cssRules;

    seltext = seltext.toLowerCase();

    for ( i = 0; i < myrules.length; i++){

        if( myrules[i].selectorText.toLowerCase() == seltext) {
            myrules[i].style.color = color;
            myrules[i].style.backgroundColor = bgcolor;
            return;
        }

    }

/*
    var rule = seltext + ": { color: " + color + "; background-color: " + bgcolor + "; }";
    alert(rule);
    alert(document.styleSheets[0].insertRule);
    document.styleSheets[0].insertRule(rule, 0);
    alert("hehe");
*/
}

function woot(elem) {
    var cssname = elem.tagName + '.' + elem.className;
    colorCssClass(cssname, "#ff0000", "#0000ff");
}

</script>

And some <reg class="foobar" onclick="colorCssClass('reg','red','blue');">red</reg> in here!

''' + r + '''
</html>
'''

app = QtGui.QApplication(sys.argv)

webView = QtWebKit.QWebView()
#webView.load(QtCore.QUrl("http://www.google.com"))
webView.setHtml(htmldoc)
webView.show()

sys.exit(app.exec_())

