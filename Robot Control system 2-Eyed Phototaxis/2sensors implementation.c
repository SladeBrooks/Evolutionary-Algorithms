#pragma config(Sensor, S1,     lightSensorR,   sensorEV3_Color, modeEV3Color_Ambient)
#pragma config(Sensor, S4,     lightSensorL,   sensorEV3_Color, modeEV3Color_Ambient)

task main()
{
	float photoL = 0;
	float photoR = 0;

	//robot loops continuously following a light source
	while (true)
	{
		//sensor values are displayed on the robot, this assists evaluating performance and testing
		displayBigTextLine( 2, "left: %d", photoL );
		displayBigTextLine( 5, "right: %d", photoR );

		//Sensor light levels are extracted
		photoL = getColorAmbient( lightSensorL )-5;//left sensor has its accuracy corrected by its accuracy offset
		photoR = getColorAmbient( lightSensorR );

		//because of the design of the robot and placement of the motors, negative values are sent to the robot in order to move it forward
		motor[motorA] = -photoR;//Left motor speed is mapped to negative right sensors light value
		motor[motorD] = -photoL;//Right motor speed is mapped to negative left sensors light value

	}
}
