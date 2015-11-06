__author__ = 'zavidan'
startpage = """
<html>
<head>
    <link href='http://fonts.googleapis.com/css?family=Poppins:400,600' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="/css/main.css">
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
</head>
<body>
    <a href="/"><div id="Logo"></div></a>
    <div>
        <a href="/" class="btn">Home</a>
        <a href="/edit" class="btn">Draw floor plan</a>
        <a href="/quick" class="btn">Room simulation</a>
        <a href="/winanalysis" class="btn">Calculate energy used</a>
        <a href="/dataentry" class="btn">House simulation</a>
    </div>
    <div>
        <a href="/pages" class="btn">Information Sources</a>
    </div>
    <h1>Home</h1>
    <p>This is a tool to simulate the amount of money and energy you save by insulating parts of your house.</p>
    <p>To make this tool work you first need to go to the "Room simulation" page and input the data it ask you for. Then hit
    the submit button and the simulation will analyse your data and simulate your house with your main room being heated
     to 18C and the rest of your house not being heated. It will give you the amount of energy and money you use to heat
     that room up for one year.<p/>
    <h3>Under Development</h3>
    <p>The Room simulation page is still under development and will become easier to use in the future.</p>
    <p>Making it so that in the Draw floor plan page you can draw your floor plan and you would get the amount of energy
    you might use in a year.</p>
    <p>Making this website mobile compatible.</p>
</body>
</html>
"""

housemade = """
<html>
<head>
    <link href='http://fonts.googleapis.com/css?family=Poppins:400,600' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="/css/edit.css">
    <link rel="stylesheet" type="text/css" href="/css/main.css">
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
    <script type="text/javascript" src="/js/house.js"></script>
</head>
<body>
    <a href="/"><div id="Logo"></div></a>
    <div>
        <a href="/" class="btn">Home</a>
        <a href="/edit" class="btn">Draw floor plan</a>
        <a href="/quick" class="btn">Room simulation</a>
        <a href="/winanalysis" class="btn">Calculate energy used</a>
        <a href="/dataentry" class="btn">House simulation</a>
    </div>
    <div>
        <a href="/pages" class="btn">Information Sources</a>
    </div>
    <h1>Draw your floor plan</h1>
    <p>The length of one blocks is 0.2 meters.</p>
    <table id="options"></table>
    <table id="tab" cellspacing="0"></table>
    <form action="/edit" method="post" id="plan">
        <input type="hidden" name="floorplan" value="{house}" id="floorplan">
        <input type="submit" id="submit" value="Save House">
    </form>
</body>
</html>
"""

dataentry = """
<html>
<head>
    <link href='http://fonts.googleapis.com/css?family=Poppins:400,600' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="/css/main.css">
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
    <script type="text/javascript" src="/js/dataentry.js"></script>
</head>
<body>
    <a href="/"><div id="Logo"></div></a>
    <div>
        <a href="/" class="btn">Home</a>
        <a href="/edit" class="btn">Draw floor plan</a>
        <a href="/quick" class="btn">Room simulation</a>
        <a href="/winanalysis" class="btn">Calculate energy used</a>
        <a href="/dataentry" class="btn">House simulation</a>
    </div>
    <div>
        <a href="/pages" class="btn">Information Sources</a>
    </div>
    <h1>House Simulation</h1>
    <h3>Under Development!</h3>
    <p>This will be a house simulation page for experts to use.</p>

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
<head>
    <link href='http://fonts.googleapis.com/css?family=Poppins:400,600' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="/css/main.css">
</head>
<body>
    <a href="/"><div id="Logo"></div></a>
    <div>
        <a href="/" class="btn">Home</a>
        <a href="/edit" class="btn">Draw floor plan</a>
        <a href="/quick" class="btn">Room simulation</a>
        <a href="/winanalysis" class="btn">Calculate energy used</a>
        <a href="/dataentry" class="btn">House simulation</a>
    </div>
    <div>
        <a href="/pages" class="btn">Information Sources</a>
    </div>
    <h1>Calculate energy used</h1>
    <div>{graph1}</div>
    <div>You use {kWh}kWhs in one year to keep the {room} warm 24/7. Thats ${money} if you are with the genesis classic anytime plan</div>
</body>
</html>
"""

quickenter = """
<html>
<head>
    <link href='http://fonts.googleapis.com/css?family=Poppins:400,600' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="/css/main.css">
</head>
<body>
    <a href="/"><div id="Logo"></div></a>
    <div>
        <a href="/" class="btn">Home</a>
        <a href="/edit" class="btn">Draw floor plan</a>
        <a href="/quick" class="btn">Room simulation</a>
        <a href="/winanalysis" class="btn">Calculate energy used</a>
        <a href="/dataentry" class="btn">House simulation</a>
    </div>
    <div>
        <a href="/pages" class="btn">Information Sources</a>
    </div>
    <h1>Room simulation</h1>
    <p>This page simulates the amount of energy you would use to keep this room warm for one year.</p>
    <form action="/quick" method="post">
        <h3>Room Names</h3>
        <p>Name of Main Room:
        <input type="text" name="main" value="{mainroom}"></p>
        <p>Rest of the House</p>
        <p>Outside</p>

        <h3>Width of the Walls</h3>
        <p>Internal wall width of the Main Room:
        <input type="number" min="0" step="any" name="Minternal" value={maininternal}></p>
        <p>External wall width of the Main Room:
        <input type="number" min="0" step="any" name="Mexternal" value={mainexternal}></p>
        <p>External wall width of the Whole House:
        <input type="number" min="0" step="any" name="Hexternal" value={fullexternal}></p>

        <h3>Area of the Windows</h3>
        <p>Area of windows in the Main Room:
        <input type="number" min="0" step="any" name="Mwindows" value={mainwinarea}></p>
        <p>Area of windows in the Whole House:
        <input type="number" min="0" step="any" name="Hwindows" value={fullwinarea}></p>

        <h3>Floor Area of Rooms</h3>
        <p>Size of Room in square meters:
        <input type="number" min="0" step="any" name="Msize" value={mainsize}></p>
        <p>Size of the Whole House in square meters:
        <input type="number" min="0" step="any" name="Hsize" value={fullsize}></p>

        <h3>R-values</h3>
        <a href="https://en.wikipedia.org/wiki/R-value_(insulation)#Example_values">Click here for common R-values</a>
        <p>Use first column of R-value table.</p>
        <p>R-value of external walls in the Main room:
        <input type="number" min="0" step="any" name="MRexternal" value={mainrexternal}></p>
        <p>R-value of windows in the Main room:
        <input type="number" min="0" step="any" name="MRwindows" value={mainrwindows}></p>
        <p>R-value of the roof in the Main room:
        <input type="number" min="0" step="any" name="MRroof" value={mainrroof}></p>
        <p>R-value of internal walls:
        <input type="number" min="0" step="any" name="Rinternal" value={rinternal}></p>
        <p>R-value of external walls:
        <input type="number" min="0" step="any" name="Rexternal" value={rexternal}></p>
        <p>R-value of windows:
        <input type="number" min="0" step="any" name="Rwindows" value={rwindows}></p>
        <p>R-value of the roof:
        <input type="number" min="0" step="any" name="Rroof" value={rroof}></p>

        <input type="submit" value="Submit Quick Entry" class="btn">
    </form>
</body>
</html>
"""

pages = """
<html>
<head>
    <link href='http://fonts.googleapis.com/css?family=Poppins:400,600' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="/css/main.css">
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
</head>
<body>
    <a href="/"><div id="Logo"></div></a>
    <div>
        <a href="/" class="btn">Home</a>
        <a href="/edit" class="btn">Draw floor plan</a>
        <a href="/quick" class="btn">Room simulation</a>
        <a href="/winanalysis" class="btn">Calculate energy used</a>
        <a href="/dataentry" class="btn">House simulation</a>
    </div>
    <div>
        <a href="/pages" class="btn">Information Sources</a>
    </div>
    <h1>Information Sources</h1>
    <a href="en.wikipedia.org/wiki/Heat_capacity">en.wikipedia.org/wiki/Heat_capacity</a>
    <p>I got the heat capacity of some common materials and formulas for my program</p>

    <a href="www.engineeringtoolbox.com/thermal-conductivity-d_429.html">www.engineeringtoolbox.com/thermal-conductivity-d_429.html</a>
    <p>I got the K-value of common building materials</p>

    <a href="https://en.wikipedia.org/wiki/R-value_(insulation)">https://en.wikipedia.org/wiki/R-value_(insulation)</a>
    <p>I got the R-value of some materials and some formulas for my program</p>

    <a>https://fr.wikipedia.org/wiki/Conductance_thermique</a>
    <p>I got the name of UA</p>

    <a href="https://en.wikipedia.org/wiki/Thermal_conduction">https://en.wikipedia.org/wiki/Thermal_conduction</a>
    <p>I got Fouriers Law</p>

    <a href="/test">Demo and Crest award page</a>
</body>
</html>
"""