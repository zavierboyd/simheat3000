__author__ = 'zavidan'
startpage = """
<html>
<head>
</head>
<body>
<a href="http://heat-simulation.appspot.com/test">Demo page</a>
<a href="http://heat-simulation.appspot.com/edit">Make/Edit your house</a>
</body>
</html>
"""
makinghouse = """
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/css/main.css">
    <script type="text/javascript" src="/js/draw.js"></script>
</head>
<body onload="house()">
    {edit}
    <table id="tab" cellspacing="0"></table>
    <form action="/edit" method="post">
        <input type="hidden" name="data" value="" id="data">
        <input type="submit" id="submit" value="Save House">
    </form>
</body>
</html>
"""
housemade = """
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/css/main.css">
    <script type="text/javascript" src="/js/house.js"></script>
</head>
<body onload="makehouse()">
    <table id="tab" cellspacing="0"></table>
    <form action="/edit" method="post">
        <input type="hidden" name="data" value="{house}" id="data">
        <input type="submit" id="submit" value="Save House">
    </form>
    <input type="button" onclick="toggle()" value"Toggle draw">
</body>
</html>
"""