#pragma config(Sensor, S1,     lightSensorR,   sensorEV3_Color, modeEV3Color_Ambient)
#pragma config(Sensor, S4,     lightSensorL,   sensorEV3_Color, modeEV3Color_Ambient)

task main()
{
	float photoL = 0;
	float photoR = 0;

	while (true)
	{
		displayBigTextLine( 2, "left: %d", photoL );
		displayBigTextLine( 5, "right: %d", photoR );
		photoL = getColorAmbient( lightSensorL );
		photoR = getColorAmbient( lightSensorR );
		if(photoL > photoR)
		{
			motor[motorA] = 5;
			motor[motorD] = -5;
		}
		if (photoL < photoR)
		{
			motor[motorA] = -5;
			motor[motorD] = 5;
		}
		else
		{
			motor[motorA] = -5;
			motor[motorD] = -5;
		}
	}
}
