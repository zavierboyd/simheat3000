__author__ = 'zavidan'
nav = """
    <a href="/"><div id="Logo"></div></a>
    <nav>
    <div class="container">
        <div class="row">
            <a href="/" class="btn col-md-3 col-sm-6 col-xs-12">Home</a>
            <a href="/house" class="btn col-md-3 col-sm-6 col-xs-12">House Dimentions</a>
            <a href="/sim" class="btn col-md-3 col-sm-6 col-xs-12">Simulation</a>
            <a href="/info" class="btn col-md-3 col-sm-6 col-xs-12">Information Sources</a>
        </div>
    </div>
    </nav>
"""

head = """
    <link href='http://fonts.googleapis.com/css?family=Poppins:400,600' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="/css/main.css">
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
"""

footer = """
    <div class="footer">
    <div class="container">
        <div class="row">
            <div class="col-md-9 hidden-xs hidden-sm"></div>
            <p class="col-md-3 col-xs-12">Web design by Zavier Boyd</p>
            <div class="col-md-9 hidden-xs hidden-sm"></div>
            <p id="copyright" class="col-md-3 col-xs-12">&copy; Copyright 2016 Simheat3000</p>
        </div>
    </div>
    </div>
"""

startpage = """
<html>
<head>
    """ + head + """
</head>
<body>
    <div class="page">
    """ + nav + """
    <div class="about">
    <div class="container">
        <h1>About</h1>
        <div class="row">
            <p class="col-xs-12">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu</p>
        </div>
    </div>
    </div>
    <div class="instruct">
    <div class="container">
        <h3>Instructions</h3>
        <div class="row">
            <p class="col-md-6 col-xs-12">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu</p>
            <img class="col-md-6 col-xs-12" src="/images/dummy.png" alt="image">
            <p class="col-md-6 col-xs-12">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu</p>
            <img class="col-md-6 col-xs-12" src="/images/dummy.png" alt="image">
        </div>
        <div class="row">
            <p class="col-md-6 col-xs-12">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu</p>
            <img class="col-md-6 col-xs-12" src="/images/dummy.png" alt="image">
            <p class="col-md-6 col-xs-12">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu</p>
            <img class="col-md-6 col-xs-12" src="/images/dummy.png" alt="image">
        </div>
    </div>
    </div>
    """ + footer + """
    </div>
</body>
</html>
"""

housemesure = """"
<html>
<head>
    """ + head + """
</head>
<body>
    <div class="page">
    """ + nav + """
    <div class="container">
    <h1>House Info</h1>

    <form action="/house" method="post">
    <h2>Width of Walls:</h2>
    <div class="row">
        <div class="col-md-4 col-xs-12">
            <h3>Room Interior Walls</h3>
            <input type="number" name="RIwall" value="{riwall}">
        </div>
        <div class="col-md-4 col-xs-12">
            <h3>Room Exterior Walls</h3>
            <input type="number" name="REwall" value="{rewall}">
        </div>
        <div class="col-md-4 col-xs-12">
            <h3>House Exterior Walls</h3>
            <input type="number" name="HEwall" value="{hewall}">
        </div>
    </div>
    <h2>Area of Windows in:</h2>
    <div class="row">
        <div class="col-md-4 col-xs-12">
            <h3>Room</h3>
            <input type="number" name="Rwindow" value="{rwindow}">
        </div>
        <div class="col-md-4 col-xs-12">
            <h3>House</h3>
            <input type="number" name="Hwindow" value="{hwindow}">
        </div>
    </div>
    <h2>Floor Area of:</h2>
    <div class="row">
        <div class="col-md-4 col-xs-12">
            <h3>Room</h3>
            <input type="number" name="Rfloor" value="{rfloor}">
        </div>
        <div class="col-md-4 col-xs-12">
            <h3>House</h3>
            <input type="number" name="Hfloor" value="{hfloor}">
        </div>
    </div>
    <br>
    <input type="submit">
    </form>
    </div>
    """ + footer + """
    </div>
</body>
</html>
"""

sim = """
<html>
<head>
    """ + head + """
    <script type="text/javascript" src="/js/simulate.js"></script>
</head>
<body>
    <div class="page">
    """ + nav + """
    <div class="container">
    <h1>Insulation</h1>
    <form id="insulation">
        <div class="row">
            <div class="col-md-3 col-sm-6 col-xs-12">
                <h2>Wall</h2>
                <h3>Room</h3>
                <div class="option">
                    <select onchange="document.getElementById('displayValue').value=this.options[this.selectedIndex].text; document.getElementById('idValue').value=this.options[this.selectedIndex].value;">
                        <option></option>
                        <option name="plywood" value="0.57">plywood</option>
                        <option name="window" value="0.57">window</option>
                        <option name="roof" value="0.57">roof</option>
                        <option name="wall" value="0.57">wall</option>
                    </select>
                    <input name="IRwall" value="{irwall}" placeholder="add/select a value" id="displayValue" onfocus="this.select()" type="number">
                </div>
                <h3>House</h3>
                <div class="option">
                    <select onchange="document.getElementById('displayValue').value=this.options[this.selectedIndex].text; document.getElementById('idValue').value=this.options[this.selectedIndex].value;">
                        <option></option>
                        <option name="plywood" value="0.57">plywood</option>
                        <option name="window" value="0.57">window</option>
                        <option name="roof" value="0.57">roof</option>
                        <option name="wall" value="0.57">wall</option>
                    </select>
                    <input name="IHwall" value="{ihwall}" placeholder="add/select a value" id="displayValue" onfocus="this.select()" type="number">
                </div>
            </div>
            <div class="col-md-3 col-sm-6 col-xs-12">
                <h2>Window</h2>
                <h3>Room</h3>
                <div class="option">
                    <select onchange="document.getElementById('displayValue').value=this.options[this.selectedIndex].text; document.getElementById('idValue').value=this.options[this.selectedIndex].value;">
                        <option></option>
                        <option name="plywood" value="0.57">plywood</option>
                        <option name="window" value="0.57">window</option>
                        <option name="roof" value="0.57">roof</option>
                        <option name="wall" value="0.57">wall</option>
                    </select>
                    <input name="IRwindow" value="{irwindow}" placeholder="add/select a value" id="displayValue" onfocus="this.select()" type="number">
                </div>
                <h3>House</h3>
                <div class="option">
                    <select onchange="document.getElementById('displayValue').value=this.options[this.selectedIndex].text; document.getElementById('idValue').value=this.options[this.selectedIndex].value;">
                        <option></option>
                        <option name="plywood" value="0.57">plywood</option>
                        <option name="window" value="0.57">window</option>
                        <option name="roof" value="0.57">roof</option>
                        <option name="wall" value="0.57">wall</option>
                    </select>
                    <input name="IHwindow" value="{ihwindow}" placeholder="add/select a value" id="displayValue" onfocus="this.select()" type="number">
                </div>
            </div>
            <div class="col-md-3 col-sm-6 col-xs-12">
                <h2>Roof</h2>
                <h3>Room</h3>
                <div class="option">
                    <select onchange="document.getElementById('displayValue').value=this.options[this.selectedIndex].text; document.getElementById('idValue').value=this.options[this.selectedIndex].value;">
                        <option></option>
                        <option name="plywood" value="0.57">plywood</option>
                        <option name="window" value="0.57">window</option>
                        <option name="roof" value="0.57">roof</option>
                        <option name="wall" value="0.57">wall</option>
                    </select>
                    <input name="IRroof" value="{irroof}" placeholder="add/select a value" id="displayValue" onfocus="this.select()" type="number">
                </div>
                <h3>House</h3>
                <div class="option">
                    <select onchange="document.getElementById('displayValue').value=this.options[this.selectedIndex].text; document.getElementById('idValue').value=this.options[this.selectedIndex].value;">
                        <option></option>
                        <option name="plywood" value="0.57">plywood</option>
                        <option name="window" value="0.57">window</option>
                        <option name="roof" value="0.57">roof</option>
                        <option name="wall" value="0.57">wall</option>
                    </select>
                    <input name="IHroof" value="{ihroof}" placeholder="add/select a value" id="displayValue" onfocus="this.select()" type="number">
                </div>
            </div>
            <div class="col-md-3 col-sm-6 col-xs-12">
                <h2>Floor</h2>
                <h3>Room</h3>
                <div class="option">
                    <select onchange="document.getElementById('displayValue').value=this.options[this.selectedIndex].text; document.getElementById('idValue').value=this.options[this.selectedIndex].value;">
                        <option></option>
                        <option name="plywood" value="0.57">plywood</option>
                        <option name="window" value="0.57">window</option>
                        <option name="roof" value="0.57">roof</option>
                        <option name="wall" value="0.57">wall</option>
                    </select>
                    <input name="IRfloor" value="{irfloor}" placeholder="add/select a value" id="displayValue" onfocus="this.select()" type="number">
                </div>
                <h3>House</h3>
                <div class="option">
                    <select onchange="document.getElementById('displayValue').value=this.options[this.selectedIndex].text; document.getElementById('idValue').value=this.options[this.selectedIndex].value;">
                        <option></option>
                        <option name="plywood" value="0.57">plywood</option>
                        <option name="window" value="0.57">window</option>
                        <option name="roof" value="0.57">roof</option>
                        <option name="wall" value="0.57">wall</option>
                    </select>
                    <input name="IHfloor" value="{ihfloor}" placeholder="add/select a value" id="displayValue" onfocus="this.select()" type="number">
                </div>
            </div>
        </div>
    </form>
    <input type="submit" value="Simulate" id="sim">
    <p><tt id="out">hi</tt></p>
    </div>
    """ + footer + """
    </div>
</body>
</html>
"""

infopage = """
<html>
<head>
    """ + head + """
</head>
<body>
    <div class="page">
    """ + nav + """
    <div class="container">
        <h1>Info</h1>
        <h2>Research</h2>
        <div class="row">
            <p>I looked at the energy calculator <a href="http://alf.branz.co.nz">Branz Annual Loss Factor(ALF)</a></p>
            <p>Then looked at some research paper but looked at one in particular <a href=""></a></p>
        </div>
        <h2>Mathematics</h2>
        <div class="row">

        </div>
        <h2>Programming</h2>
        <div class="row">

        </div>
    </div>
    """ + footer + """
    </div>
</body>
</html>
"""
## Old ##
#startpage = """
#<html>
#<head>
#    """ + head + """
#</head>
#<body>
#    <div class="page">
#    """ + nav + """
#    <h1>Home</h1>
#    <p>This is a tool to simulate.js the amount of money and energy you save by insulating parts of your house.</p>
#    <p>To make this tool work you first need to go to the "Room simulation" page and input the data it ask you for. Then hit
#    the submit button and the simulation will analyse your data and simulate.js your house with your main room being heated
#     to 18C and the rest of your house not being heated. It will give you the amount of energy and money you use to heat
#     that room up for one year.<p/>
#    <h3>Under Development</h3>
#    <p>The Room simulation page is still under development and will become easier to use in the future.</p>
#    <p>Making it so that in the Draw floor plan page you can draw your floor plan and you would get the amount of energy
#    you might use in a year.</p>
#    <p>Making this website mobile compatible.</p>
#    </div>
#</body>
#</html>
#"""

housemade = """
<html>
<head>
    """ + head + """
    <link rel="stylesheet" type="text/css" href="/css/edit.css">
    <script type="text/javascript" src="/js/house.js"></script>
</head>
<body>
    <div class="page">
    """ + nav + """
    <h1>Draw your floor plan</h1>
    <p>The length of one blocks is 0.2 meters.</p>
    <table id="options"></table>
    <table id="tab" cellspacing="0"></table>
    <form action="/edit" method="post" id="plan">
        <input type="hidden" name="floorplan" value="{house}" id="floorplan">
        <input type="submit" id="submit" value="Save House">
    </form>
    """ + footer + """
    </div>
</body>
</html>
"""

dataentry = """
<html>
<head>
    """ + head + """
    <script type="text/javascript" src="/js/dataentry.js"></script>
</head>
<body>
    <div class="page">
    """ + nav + """
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
    """ + footer + """
    </div>
</body>
</html>
"""

analysis = """
<html>
<head>
    """ + head + """
</head>
<body>
    <h1>Calculate energy used</h1>
    <div>You use {kWh}kWhs in one year to keep the {room} warm 24/7. Thats ${money} if you are with the genesis classic anytime plan</div>
    <div>{graph1}</div>
</body>
</html>
"""

quickenter = """
<html>
<head>
    """ + head + """
</head>
<body>
    <div class="page">
    """ + nav + """
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
        <p>Size of the Main Room in square meters:
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
        <p>R-value of internal walls in the Main room:
        <input type="number" min="0" step="any" name="Rinternal" value={rinternal}></p>
        <p>R-value of external walls in the Whole House:
        <input type="number" min="0" step="any" name="Rexternal" value={rexternal}></p>
        <p>R-value of windows in the Whole House:
        <input type="number" min="0" step="any" name="Rwindows" value={rwindows}></p>
        <p>R-value of the roof in the Whole House:
        <input type="number" min="0" step="any" name="Rroof" value={rroof}></p>
        <input type="submit" value="Submit Quick Entry" class="btn">
    </form>
    """ + footer + """
    </div>
</body>
</html>
"""

pages = """
<html>
<head>
    """ + head + """
</head>
<body>
    <div class="page">
    """ + nav + """
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
    """ + footer + """
    </div>
</body>
</html>
"""