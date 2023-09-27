from tkinter import *

geometryX = 340
geometryY = 250


def raise_frame(frame):
    frame.tkraise()


class FormulaCalculator:
    def __init__(self, master):
        master.title("Formula Calculator")
        master.minsize(geometryX, geometryY)
        master.maxsize(geometryX, geometryY)

        self.velocity = Frame(master)
        self.force = Frame(master)
        self.work = Frame(master)
        self.pressure = Frame(master)
        self.potentialenergy = Frame(master)
        self.trapeziod = Frame(master)
        self.rectangle = Frame(master)
        self.triangle = Frame(master)
        self.cylinder = Frame(master)
        self.cycle = Frame(master)

        for frame in (self.velocity, self.force, self.work, self.pressure, self.potentialenergy,
                      self.trapeziod, self.rectangle, self.triangle, self.cylinder, self.cycle):
            frame.grid(row=0, column=0, sticky='news')

        # ==============================================================================================================
        # ======================= Velocity Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.veTitleLabel = Label(self.velocity, text="Velocity").grid(row=0, column=1)
        self.veDistanceLabel = Label(self.velocity, text="Distance (m): ").grid(row=1, column=0)
        self.veTimeLabel = Label(self.velocity, text="Time (s): ").grid(row=2, column=0)
        self.veVelocityLabel = Label(self.velocity, text="Velocity (m/s):  ").grid(row=3, column=0)

        # Entry boxes
        self.veDistance = Entry(self.velocity)
        self.veTime = Entry(self.velocity)
        self.veVelocity = Entry(self.velocity)

        # Packing the entry boxes into the frame
        self.veDistance.grid(row=1, column=1)
        self.veTime.grid(row=2, column=1)
        self.veVelocity.grid(row=3, column=1)

        # Button and packing
        self.veConvertVelocity = Button(self.velocity, text="Calculate Velocity",
                                        command=self.velocityCalcVelocity).grid(row=4, column=1)
        self.veConvertDistance = Button(self.velocity, text="Calculate Distance",
                                        command=self.velocityCalcDistance).grid(row=5, column=1)
        self.veConvertTime = Button(self.velocity, text="Calculate Time", command=self.velocityCalcTime).grid(row=6,
                                                                                                              column=1)

        # ==============================================================================================================
        # ======================= Force Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.foTitleLabel = Label(self.force, text="Force").grid(row=0, column=1)
        self.foAccelerationLabel = Label(self.force, text="Acceleration (m/s**2): ").grid(row=1, column=0)
        self.foMassLabel = Label(self.force, text="Mass (kg): ").grid(row=2, column=0)
        self.foForceLabel = Label(self.force, text="Force (N): ").grid(row=3, column=0)

        # Entry boxes
        self.foAcceleration = Entry(self.force)
        self.foMass = Entry(self.force)
        self.foForce = Entry(self.force)

        # Entry packing
        self.foAcceleration.grid(row=1, column=1)
        self.foMass.grid(row=2, column=1)
        self.foForce.grid(row=3, column=1)

        # Buttons and packing
        self.foConvertAcceleration = Button(self.force, text="Calculate Acceleration", command=self.foCalcAcceleration)
        self.foConvertMass = Button(self.force, text="Calculate Mass", command=self.foCalcMass)
        self.foConvertForce = Button(self.force, text="Calculate Force", command=self.foCalcForce)

        self.foConvertAcceleration.grid(row=4, column=1)
        self.foConvertMass.grid(row=5, column=1)
        self.foConvertForce.grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Work Menu Layout ===================================================================
        # ==============================================================================================================

        # Labels
        self.woTitleLabel = Label(self.work, text="Work").grid(row=0, column=1)
        self.woDistanceLabel = Label(self.work, text="Distance (m): ").grid(row=1, column=0)
        self.woForceLabel = Label(self.work, text="Force (N): ").grid(row=2, column=0)
        self.woWorkdoneLabel = Label(self.work, text="Workdone (N/m): ").grid(row=3, column=0)

        # Entry Boxes
        self.woDistance = Entry(self.work)
        self.woForce = Entry(self.work)
        self.woWork = Entry(self.work)

        # Entry packing
        self.woDistance.grid(row=1, column=1)
        self.woForce.grid(row=2, column=1)
        self.woWork.grid(row=3, column=1)

        self.woConvertDistance = Button(self.work, text="Calculate Distance", command=self.woCalcDistance)
        self.woConvertForce = Button(self.work, text="Calculate Force", command=self.woCalcForce)
        self.woConvertWorkdone = Button(self.work, text="Calculate Workdone", command=self.woCalcWorkdone)

        self.woConvertDistance.grid(row=4, column=1)
        self.woConvertForce.grid(row=5, column=1)
        self.woConvertWorkdone.grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Pressure Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.prTitleLabel = Label(self.pressure, text="Pressure").grid(row=0, column=1)
        self.prForceLabel = Label(self.pressure, text="Force (N): ").grid(row=1, column=0)
        self.prAreaLabel = Label(self.pressure, text="Area (m**2): ").grid(row=2, column=0)
        self.prPressureLabel = Label(self.pressure, text="Pressure (N/m**2): ").grid(row=3, column=0)

        # Entry boxes
        self.prForce = Entry(self.pressure)
        self.prArea = Entry(self.pressure)
        self.prPressure = Entry(self.pressure)

        # Entry packing
        self.prForce.grid(row=1, column=1)
        self.prArea.grid(row=2, column=1)
        self.prPressure.grid(row=3, column=1)

        # Buttons and packing
        self.prConvertForce = Button(self.pressure, text="Calculate Force", command=self.prCalcForce)
        self.prConvertArea = Button(self.pressure, text="Calculate Area", command=self.prCalcArea)
        self.prConvertPressure = Button(self.pressure, text="Calculate Pressure", command=self.prCalcPressure)

        self.prConvertForce.grid(row=4, column=1)
        self.prConvertArea.grid(row=5, column=1)
        self.prConvertPressure.grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Potentialenergy Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.poTitleLabel = Label(self.potentialenergy, text="Potential Energy").grid(row=0, column=1)
        self.poMassLabel = Label(self.potentialenergy, text="Mass (kg): ").grid(row=1, column=0)
        self.poHeightLabel = Label(self.potentialenergy, text="Height (m): ").grid(row=2, column=0)
        self.poGravityLabel = Label(self.potentialenergy, text="Gravity: ").grid(row=3, column=0)
        self.poPotentialenergyLabel = Label(self.potentialenergy, text="Potential Energy (N/m**2): ").grid(row=4,
                                                                                                           column=0)

        # Entry boxes
        self.poMass = Entry(self.potentialenergy)
        self.poHeight = Entry(self.potentialenergy)
        self.poGravity = Entry(self.potentialenergy)
        self.poPotentialenergy = Entry(self.potentialenergy)

        # Entry packing
        self.poMass.grid(row=1, column=1)
        self.poHeight.grid(row=2, column=1)
        self.poGravity.grid(row=3, column=1)
        self.poPotentialenergy.grid(row=4, column=1)

        # Buttons and packing
        self.poConvertMass = Button(self.potentialenergy, text="Calculate Mass", command=self.poCalcMass)
        self.poConvertHeight = Button(self.potentialenergy, text="Calculate Height", command=self.poCalcHeight)
        self.poConvertGravity = Button(self.potentialenergy, text="Calculate Gravity", command=self.poCalcGravity)
        self.poConvertPotentialenergy = Button(self.potentialenergy, text="Calculate Potentialenergy",
                                               command=self.poCalcPotentialenergy)

        self.poConvertMass.grid(row=5, column=1)
        self.poConvertHeight.grid(row=6, column=1)
        self.poConvertGravity.grid(row=7, column=1)
        self.poConvertPotentialenergy.grid(row=8, column=1)

        # ==============================================================================================================
        # ======================= Trapeziod Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.trTitleLabel = Label(self.trapeziod, text="Area of Trapeziod").grid(row=0, column=1)
        self.trForceLabel = Label(self.trapeziod, text="Base (cm)): ").grid(row=1, column=0)
        self.trAreaLabel = Label(self.trapeziod, text="Length (cm): ").grid(row=2, column=0)
        self.trPressureLabel = Label(self.trapeziod, text="Area of Trapeziod (cm**2): ").grid(row=3, column=0)

        # Entry boxes
        self.trBase = Entry(self.trapeziod)
        self.trLength = Entry(self.trapeziod)
        self.trTrapeziod = Entry(self.trapeziod)

        # Entry packing
        self.trBase.grid(row=1, column=1)
        self.trLength.grid(row=2, column=1)
        self.trTrapeziod.grid(row=3, column=1)

        # Buttons and packing
        self.trConvertBase = Button(self.trapeziod, text="Calculate Base", command=self.trCalcBase)
        self.trConvertLength = Button(self.trapeziod, text="Calculate Length", command=self.trCalcLength)
        self.trConvertTrapeziod = Button(self.trapeziod, text="Calculate Trapeziod", command=self.trCalcTrapeziod)

        self.trConvertBase.grid(row=4, column=1)
        self.trConvertLength.grid(row=5, column=1)
        self.trConvertTrapeziod.grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Rectangle Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.reTitleLabel = Label(self.rectangle, text="Area of Rectangle").grid(row=0, column=1)
        self.reWidthLabel = Label(self.rectangle, text="Width (cm)): ").grid(row=1, column=0)
        self.reLengthLabel = Label(self.rectangle, text="Length (cm): ").grid(row=2, column=0)
        self.reRectangleLabel = Label(self.rectangle, text="Area of Rectangle (cm**2): ").grid(row=3, column=0)

        # Entry boxes
        self.reWidth = Entry(self.rectangle)
        self.reLength = Entry(self.rectangle)
        self.reRectangle = Entry(self.rectangle)

        # Entry packing
        self.reWidth.grid(row=1, column=1)
        self.reLength.grid(row=2, column=1)
        self.reRectangle.grid(row=3, column=1)

        # Buttons and packing
        self.reConvertWidth = Button(self.rectangle, text="Calculate width", command=self.reCalcWidth)
        self.reConvertLength = Button(self.rectangle, text="Calculate Length", command=self.reCalcLength)
        self.reConvertRectangle = Button(self.rectangle, text="Calculate Area of Rectangle",
                                         command=self.reCalcRectangle)

        self.reConvertWidth.grid(row=4, column=1)
        self.reConvertLength.grid(row=5, column=1)
        self.reConvertRectangle.grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Triangle Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.triTitleLabel = Label(self.triangle, text="Area of Triangle").grid(row=0, column=1)
        self.triBaseLabel = Label(self.triangle, text="Base (cm)): ").grid(row=1, column=0)
        self.triHeightLabel = Label(self.triangle, text="Height (cm): ").grid(row=2, column=0)
        self.triTriangleLabel = Label(self.triangle, text="Area of Triangle (cm**2): ").grid(row=3, column=0)

        # Entry boxes
        self.triBase = Entry(self.triangle)
        self.triHeight = Entry(self.triangle)
        self.triTriangle = Entry(self.triangle)

        # Entry packing
        self.triBase.grid(row=1, column=1)
        self.triHeight.grid(row=2, column=1)
        self.triTriangle.grid(row=3, column=1)

        # Buttons and packing
        self.triConvertBase = Button(self.triangle, text="Calculate Base", command=self.triCalcBase)
        self.triConvertHeight = Button(self.triangle, text="Calculate Height", command=self.triCalcHeight)
        self.triConvertTriangle = Button(self.triangle, text="Calculate Area of Triangle", command=self.triCalcTriangle)

        self.triConvertBase.grid(row=4, column=1)
        self.triConvertHeight.grid(row=5, column=1)
        self.triConvertTriangle.grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Cycle Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.cycTitleLabel = Label(self.cycle, text="Area of Cycle ").grid(row=0, column=1)
        self.cycPiLabel = Label(self.cycle, text="Pi : ").grid(row=1, column=0)
        self.cycRadiusLabel = Label(self.cycle, text="Radius (cm): ").grid(row=2, column=0)
        self.cycCycleLabel = Label(self.cycle, text="Area of Cycle (cm**2): ").grid(row=3, column=0)

        # Entry boxes
        self.cycPi = Entry(self.cycle)
        self.cycRadius = Entry(self.cycle)
        self.cycCycle = Entry(self.cycle)

        # Entry packing
        self.cycPi.grid(row=1, column=1)
        self.cycRadius.grid(row=2, column=1)
        self.cycCycle.grid(row=3, column=1)

        # Buttons and packing
        self.cycConvertRadius = Button(self.cycle, text="Calculate Radius", command=self.cycCalcRadius)
        self.cycConvertPi = Button(self.cycle, text="Calculate Pi", command=self.cycCalcPi)
        self.cycConvertCycle = Button(self.cycle, text="Calculate Area of Cycle", command=self.cycCalcCycle)

        self.cycConvertRadius.grid(row=4, column=1)
        self.cycConvertPi.grid(row=5, column=1)
        self.cycConvertCycle.grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Cylinder Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.cyTitleLabel = Label(self.cylinder, text="Area of Cylinder ").grid(row=0, column=1)
        self.cyPiLabel = Label(self.cylinder, text="Radius (cm) : ").grid(row=1, column=0)
        self.cyRadiusLabel = Label(self.cylinder, text="Pi : ").grid(row=2, column=0)
        self.cyHeightLabel = Label(self.cylinder, text="Height (cm): ").grid(row=3, column=0)
        self.cyCycleLabel = Label(self.cylinder, text="Area of Cylinder (cm**2): ").grid(row=4, column=0)

        # Entry boxes
        self.cyRadius = Entry(self.cylinder)
        self.cyPi = Entry(self.cylinder)
        self.cyHeight = Entry(self.cylinder)
        self.cyCylinder = Entry(self.cylinder)

        # Entry packing
        self.cyRadius.grid(row=1, column=1)
        self.cyPi.grid(row=2, column=1)
        self.cyHeight.grid(row=3, column=1)
        self.cyCylinder.grid(row=4, column=1)

        # Buttons and packing
        self.cyConvertRadius = Button(self.cylinder, text="Calculate Radius", command=self.cyCalcRadius)
        self.cyConvertPi = Button(self.cylinder, text="Calculate Pi", command=self.cyCalcPi)
        self.cyConvertHeight = Button(self.cylinder, text="Calculate Height", command=self.cyCalcHeight)
        self.cyConvertCylinder = Button(self.cylinder, text="Calculate Area of Cylinder", command=self.cyCalcCylinder)

        self.cyConvertRadius.grid(row=5, column=1)
        self.cyConvertPi.grid(row=6, column=1)
        self.cyConvertHeight.grid(row=7, column=1)
        self.cyConvertCylinder.grid(row=8, column=1)

        # ==============================================================================================================
        # ========================= Menu bar Layout ====================================================================
        # ==============================================================================================================
        self.menubar = Menu(master)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=master.destroy)

        self.insertmenu = Menu(self.menubar, tearoff=0)
        self.insertmenu.add_command(label="Earth's Gravity Constant", command=self.insertGravity)
        self.insertmenu.add_command(label="Pi", command=self.insertPi)
        self.insertmenu.add_command(label="Pi", command=self.insertpi)

        self.physics = Menu(self.menubar, tearoff=0)
        self.physics.add_command(label="FORCES")
        self.physics.add_separator()
        self.physics.add_command(label="Velocity", command=lambda: raise_frame(self.velocity))
        self.physics.add_command(label="Force", command=lambda: raise_frame(self.force))
        self.physics.add_command(label="Work", command=lambda: raise_frame(self.work))
        self.physics.add_command(label="Pressure", command=lambda: raise_frame(self.pressure))
        self.physics.add_command(label="Potentialenergy", command=lambda: raise_frame(self.potentialenergy))

        self.maths = Menu(self.menubar, tearoff=0)
        self.maths.add_command(label="AREAS")
        self.maths.add_separator()
        self.maths.add_command(label="Area: Trapeziod", command=lambda: raise_frame(self.trapeziod))
        self.maths.add_command(label="Area: Rectangle", command=lambda: raise_frame(self.rectangle))
        self.maths.add_command(label="Area: Triangle", command=lambda: raise_frame(self.triangle))
        self.maths.add_command(label="Area: Cylinder", command=lambda: raise_frame(self.cylinder))
        self.maths.add_command(label="Area: Cycle", command=lambda: raise_frame(self.cycle))

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Insert", menu=self.insertmenu)
        self.menubar.add_cascade(label="Physics", menu=self.physics)
        self.menubar.add_cascade(label="Maths", menu=self.maths)

        master.config(menu=self.menubar)

    # ============================ INSERT FUNCTIONS ====================================================================

    def insertGravity(self):
        raise_frame(self.potentialenergy)
        self.poGravity.delete(0, END)
        self.poGravity.insert(INSERT, "9.81")

    def insertpi(self):
        raise_frame(self.cylinder)
        self.cyPi.delete(0, END)
        self.cyPi.insert(INSERT, "3.143")

    def insertPi(self):
        raise_frame(self.cycle)
        self.cycPi.delete(0, END)
        self.cycPi.insert(INSERT, "3.143")

    # ==================================================================================================================
    # ======================= Logical Processes ========================================================================
    # ==================================================================================================================

    """ Velocity CALCULATIONS """

    def velocityCalcVelocity(self):
        self._distance = float(self.veDistance.get())
        self._time = float(self.veTime.get())

        self.veVelocity.delete(0, END)
        self.veVelocity.insert(INSERT, str(self._distance / self._time))

    def velocityCalcTime(self):
        self._distance = float(self.veDistance.get())
        self._velocity = float(self.veVelocity.get())

        self.veTime.delete(0, END)
        self.veTime.insert(INSERT, str(self._distance / self._velocity))

    def velocityCalcDistance(self):
        self._velocity = float(self.veVelocity.get())
        self._time = float(self.veTime.get())

        self.veDistance.delete(0, END)
        self.veDistance.insert(INSERT, str(self._time * self._velocity))

    """ Force CALCULATIONS """

    def foCalcAcceleration(self):
        self._mass = float(self.foMass.get())
        self._force = float(self.foForce.get())

        self.foAcceleration.delete(0, END)
        self.foAcceleration.insert(INSERT, str(self._force / self._mass))

    def foCalcMass(self):
        self._acceleration = float(self.foAcceleration.get())
        self._force = float(self.foForce.get())

        self.foMass.delete(0, END)
        self.foMass.insert(INSERT, str(self._force / self._acceleration))

    def foCalcForce(self):
        self._mass = float(self.foMass.get())
        self._acceleration = float(self.foAcceleration.get())

        self.foForce.delete(0, END)
        self.foForce.insert(INSERT, str(self._mass * self._acceleration))

    """ Work Calculations """

    def woCalcDistance(self):
        self._force = float(self.woForce.get())
        self._work = float(self.woWork.get())

        self.woDistance.delete(0, END)
        self.woDistance.insert(INSERT, str(self._work / self._force))

    def woCalcForce(self):
        self._distance = float(self.woDistance.get())
        self._work = float(self.woWork.get())

        self.woForce.delete(0, END)
        self.woForce.insert(INSERT, str(self._work / self._distance))

    def woCalcWorkdone(self):
        self._distance = float(self.woDistance.get())
        self._force = float(self.woForce.get())

        self.woWork.delete(0, END)
        self.woWork.insert(INSERT, str(self._force * self._distance))

    """ Pressure Calculations """

    def prCalcForce(self):
        self._pressure = float(self.prPressure.get())
        self._area = float(self.prArea.get())

        self.prForce.delete(0, END)
        self.prForce.insert(INSERT, str(self._pressure / self._area))

    def prCalcArea(self):
        self._pressure = float(self.prPressure.get())
        self._force = float(self.prForce.get())

        self.prArea.delete(0, END)
        self.prArea.insert(INSERT, str(self._pressure / self._force))

    def prCalcPressure(self):
        self._area = float(self.prArea.get())
        self._force = float(self.prForce.get())

        self.prPressure.delete(0, END)
        self.prPressure.insert(INSERT, str(self._area * self._force))

    """ Potential Energy Calculations """

    def poCalcMass(self):
        self._potentialenergy = float(self.poPotentialenergy.get())
        self._height = float(self.poHeight.get())
        self._gravity = float(self.poGravity.get())

        self.poPotentialenergy.delete(0, END)
        self.poPotentialenergy.insert(INSERT, str(self._potentialenergy / self._height * self._gravity))

    def poCalcHeight(self):
        self._potentialenergy = float(self.poPotentialenergy.get())
        self._mass = float(self.poMass.get())
        self._gravity = float(self.poGravity.get())

        self.poHeight.delete(0, END)
        self.poHeight.insert(INSERT, str(self._potentialenergy / self._mass * self._gravity))

    def poCalcGravity(self):
        self._potentialenergy = float(self.poPotentialenergy.get())
        self._mass = float(self.poMass.get())
        self._height = float(self.poHeight.get())

        self.poGravity.delete(0, END)
        self.poGravity.insert(INSERT, str(self._potentialenergy / self._mass * self._height))

    def poCalcPotentialenergy(self):
        self._mass = float(self.poMass.get())
        self._height = float(self.poHeight.get())
        self._gravity = float(self.poGravity.get())

        self.poPotentialenergy.delete(0, END)
        self.poPotentialenergy.insert(INSERT, str(self._mass * self._height * self._gravity))

    """ Trapeziod Calculations """

    def trCalcBase(self):
        self._length = float(self.trLength.get())
        self._trapeziod = float(self.trTrapeziod.get())

        self.trBase.delete(0, END)
        self.trBase.insert(INSERT, str(2 * self._trapeziod - self._length))

    def trCalcLength(self):
        self._base = float(self.trBase.get())
        self._trapeziod = float(self.trTrapeziod.get())

        self.trLength.delete(0, END)
        self.trLength.insert(INSERT, str(2 * self._trapeziod - self._base))

    def trCalcTrapeziod(self):
        self._base = float(self.trBase.get())
        self._length = float(self.trLength.get())

        self.trTrapeziod.delete(0, END)
        self.trTrapeziod.insert(INSERT, str((self._base + self._length) / 2))

    """ Rectangle Calculations """

    def reCalcWidth(self):
        self._length = float(self.reLength.get())
        self._rectangle = float(self.reRectangle.get())

        self.reWidth.delete(0, END)
        self.reWidth.insert(INSERT, str(self._rectangle / self._length))

    def reCalcLength(self):
        self._width = float(self.reWidth.get())
        self._rectangle = float(self.reRectangle.get())

        self.reLength.delete(0, END)
        self.reLength.insert(INSERT, str(self._rectangle / self._width))

    def reCalcRectangle(self):
        self._width = float(self.reWidth.get())
        self._length = float(self.reLength.get())

        self.reRectangle.delete(0, END)
        self.reRectangle.insert(INSERT, str(self._width * self._length))

    """ Triangle Calculations """

    def triCalcBase(self):
        self._height = float(self.triHeight.get())
        self._triangle = float(self.triTriangle.get())

        self.triBase.delete(0, END)
        self.triBase.insert(INSERT, str(2 * self._triangle / self._height))

    def triCalcHeight(self):
        self._base = float(self.triBase.get())
        self._triangle = float(self.triTriangle.get())

        self.triHeight.delete(0, END)
        self.triHeight.insert(INSERT, str(2 * self._triangle / self._base))

    def triCalcTriangle(self):
        self._base = float(self.triBase.get())
        self._height = float(self.triHeight.get())

        self.triTriangle.delete(0, END)
        self.triTriangle.insert(INSERT, str((self._base * self._height) / 2))

    """ Cycle Calculations """

    def cycCalcRadius(self):
        self._Pi = float(self.cycPi.get())
        self._cycle = float(self.cycCycle.get())

        self.cycRadius.delete(0, END)
        self.cycRadius.insert(INSERT, str(sqrt(self._cycle / self._Pi)))

    def cycCalcPi(self):
        self._radius = float(self.cycRadius.get())
        self._cycle = float(self.cycCycle.get())

        self.cycPi.delete(0, END)
        self.cycPi.insert(INSERT, str(self._cycle / self._radius * self._radius))

    def cycCalcCycle(self):
        self._radius = float(self.cycRadius.get())
        self._Pi = float(self.cycPi.get())

        self.cycCycle.delete(0, END)
        self.cycCycle.insert(INSERT, str(self._Pi * self._radius * self._radius))

    """ Cylinder Calculations """

    def cyCalcRadius(self):
        self._pi = float(self.cyPi.get())
        self._Height = float(self.cyHeight.get())
        self._cylinder = float(self.cyCylinder.get())

        self.cyRadius.delete(0, END)
        self.cyRadius.insert(INSERT, str(self._pi * self._Height +
                                         sqrt((self._pi * self._Height) ** 2 + 2 * self._pi * self._cylinder
                                              ) / 2 * self._pi))

    def cyCalcPi(self):
        self._Radius = float(self.cyRadius.get())
        self._Height = float(self.cyHeight.get())
        self._cylinder = float(self.cyCycle.get())

        self.cyPi.delete(0, END)
        self.cyPi.insert(INSERT, str(self._cylinder / 2 * self._Radius * self._Height +
                                     2 * self._Radius * self._Radius))

    def cyCalcHeight(self):
        self._Radius = float(self.cyRadius.get())
        self._pi = float(self.cypi.get())
        self._cylinder = float(self.cyCylinder.get())

        self.cyHeight.delete(0, END)
        self.cyHeight.insert(INSERT, str(self._cylinder + 2 * self._pi * self._Radius * self._Radius /
                                         2 * self._pi * self._Radius * self._Radius))

    def cyCalcCylinder(self):
        self._Radius = float(self.cyRadius.get())
        self._Height = float(self.cyHeight.get())
        self._pi = float(self.cyPi.get())

        self.cyCylinder.delete(0, END)
        self.cyCylinder.insert(INSERT, str(2 * self._pi * self._Radius * self._Height
                                           + 2 * self._pi * self._Radius * self._Radius))


root = Tk()
main = FormulaCalculator(root)
root.mainloop()
