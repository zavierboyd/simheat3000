__author__ = 'zavidan'
startpage = """
<html>
<head>
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
</head>
<body>
    <div>
        <a href="/test">Demo page</a>
        <a href="/edit">Make/Edit your house</a>
        <a href="/dataentry">Manual Data entry</a>
        <a href="/analysisnppower">Analysis</a>
    </div>
</body>
</html>
"""

housemade = """
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/css/edit.css">
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
    <script type="text/javascript" src="/js/house.js"></script>
</head>
<body>
    <table id="tab" cellspacing="0"></table>
    <form action="/edit" method="post" id="plan">
        <input type="hidden" name="floorplan" value="{house}" id="floorplan">
        <input type="submit" id="submit" value="Save House">
    </form>
    <table id="options"></table>
    <a href="/">Back to main page</a>
</body>
</html>
"""

dataentry = """
<html>
<head>
    <!--<link rel="stylesheet" type="text/css" href="/css/edit.css">-->
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
    <script type="text/javascript" src="/js/dataentry.js"></script>
</head>
<body>
    <div>
        <a href="/">Back to main page</a>
    </div>
    <form action="/dataentry" method="post" id="house">
        <p>Room Names</p>
        <table id="names"></table>
        <p>Initial Temperatures</p>
        <table id="temps"></table>
        <p>U-Values of the Walls</p>
        <table id="conductance"></table>
        <p>Width of the Walls</p>
        <table id="area"></table>
        <p>Heat Capacity</p>
        <table id="capacity"></table>
        <input type="hidden" id="tarea" name="tarea">
        <input type="hidden" id="tnames" name="tnames">
        <input type="hidden" id="ttemps" name="ttemps">
        <input type="hidden" id="tconductance" name="tconductance">
        <input type="hidden" id="tcapacity" name="tcapacity">
        <input type="submit">
    </form>
    <input type="hidden" id="pyarea" name="pyarea" value="{pyarea}">
    <input type="hidden" id="pynames" name="pynames" value="{pynames}">
    <input type="hidden" id="pytemps" name="pytemps" value="{pytemps}">
    <input type="hidden" id="pyconductance" name="pyconductance" value="{pyconductance}">
    <input type="hidden" id="pycapacity" name="pycapacity" value="{pycapacity}">
</body>
</html>
"""

analysis = """
<html>
<head></head>
<body>
    <div>{graph1}</div>
    <div><a href="/">Back to main page</a></div>
</body>
</html>
"""

analysisnograph="""
<html>
<head></head>
<body>
    <div>{graph1}</div>
    <div><a href="/">Back to main page</a></div>
</body>
</html>
"""