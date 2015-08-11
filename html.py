__author__ = 'zavidan'
main = """
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/css/main.css">
    <script type="text/javascript" src="/js/draw.js"></script>
</head>
<body onload="house()">
    <table id="tab" cellspacing="0"></table>
    <form action="/" method="post">
        <input type="button" value="Finished House!" onclick="sendData()">
        <input type="hidden" name="data" value="" id="data">
        <input type="hidden" id="submit" value="Submit House">
    </form>
</body>
</html>
"""