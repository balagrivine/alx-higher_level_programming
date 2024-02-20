#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
	if (err)
	{
		console.error(err);
	}

	const taskData = JSON.parse(body);

	const completedTasks = taskData.filter(task =>task.completed);

	const completedTaskByUser = {};

	completedTasks.forEach(task => {
		const userId = task.userId;
		if (completedTaskByUser.hasOwnProperty(userId)) {
			completedTaskByUser[userId] += 1;
		}
		else
		{
			completedTaskByUser[userId] = 1;
		}
	});

	/*completedTaskByUser.forEach((count, userId) => {
		console.log(`${userId} ${count}`);
	});*/
	const jsonString = JSON.stringify(completedTaskByUser);
	console.log(jsonString);
});
