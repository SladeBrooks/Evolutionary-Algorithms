#pragma config(Sensor, S1,     lightSensor,   sensorEV3_Color, modeEV3Color_Ambient)

//The robot rotates over 360 degrees saving the strongest light source as it goes
//returns: strongest light level found
float findStrongest()
{
	float photo = 0.0;
	displayBigTextLine( 2, "checking: %d", photo );//displats current phase

	//starts the robot turning
	motor[motorA] = 20;
	motor[motorD] = -20;

	//iterates for 4200 milliseconds, through preliminary tests this ensures that enough time has passed for the robot have rotated about 400 degrees.(depends on surface friction)
	for ( int i = 0; i < 4200; i = i +1 ) {
		float current = getColorAmbient( lightSensor );
		if(current > photo)
		{
			photo = current;//every millisecond interval, if the current light level is the largest seen, then it is saved as the strongest
		}
   	wait1Msec(1);
	}
	return photo;
}

//the robot turns until it finds the target light source level then moves forward once it has found the target light level, once the target light level reduces, the method ends.
//param: target, the target light level the robot is looking for
void seek(float target)
{
	float current = 0.0	;
	int maxTime = 4200;
	int time = 0;
	while ((current <= target-1)&& time < maxTime)
	{
		displayBigTextLine( 2, "seeking: %d", current );//displays current phase
		time++;
		current = getColorAmbient( lightSensor );
		motor[motorA] = -20;
		motor[motorD] = 20;
		wait1Msec(1);
	}
	while(current >= target-1)
	{
		displayBigTextLine( 2, "moving: %d", current );
		current = getColorAmbient( lightSensor );
		motor[motorA] = -20;
		motor[motorD] = -20;
	}
}










task main()
{
	float strongest = 0.0;
	displayBigTextLine( 2, "Strongest: %d", strongest );//displays Strongest

	//set the motors to stop and wait for a second because it becomes more aparent what phase the bot is in
	motor[motorA] = 0;
	motor[motorD] = 0;
	wait1Msec(1000);

	//The main loop continually repeats the proccess of
	//	1.finding the strongest light source by rotating
	//	2.seeking that strongest light source until it reduces
	//we implemented wait intervals between each phase in order to better understand the current phase
	while (true)
	{
		strongest = findStrongest();//Finds the strongest light source
		//set the motors to stop and wait for a second because it becomes more aparent what phase the bot is in
	motor[motorA] = 0;
	motor[motorD] = 0;
	wait1Msec(1000);
		seek(strongest);
		//set the motors to stop and wait for a second because it becomes more aparent what phase the bot is in
	motor[motorA] = 0;
	motor[motorD] = 0;
	wait1Msec(1000);
	}
}
