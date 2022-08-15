0x03. Queuing System in JS
==========================

Back-endJavaScriptES6RedisNodeJSExpressJSKue

-   By: Johann Kerbrat, Engineering Manager at Uber Works
-   Weight: 1

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/1486e02a78cdf7b4557c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220815T195509Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=35ec3a36d25c73a134fb0de3065010e6c5f93cba917db5eebd0ee999f3a10511)

Resources
---------

**Read or watch**:

-   [Redis quick start](https://alx-intranet.hbtn.io/rltoken/8xeApIhnxgFZkgn54BiIeA "Redis quick start")
-   [Redis client interface](https://alx-intranet.hbtn.io/rltoken/1rq3ral-3C5O1t67dbGcWg "Redis client interface")
-   [Redis client for Node JS](https://alx-intranet.hbtn.io/rltoken/mRftfl67BrNvl-RM5JQfUA "Redis client for Node JS")
-   [Kue](https://alx-intranet.hbtn.io/rltoken/yTC3Ci2IV2US24xJsBfMgQ "Kue") *deprecated but still use in the industry*

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/7yh7c3Zyy1RyUsdwlfsyDg "explain to anyone"), **without the help of Google**:

-   How to run a Redis server on your machine
-   How to run simple operations with the Redis client
-   How to use a Redis client with Node JS for basic operations
-   How to store hash values in Redis
-   How to deal with async operations with Redis
-   How to use Kue as a queue system
-   How to build a basic Express app interacting with a Redis server
-   How to the build a basic Express app interacting with a Redis server and queue

Requirements
------------

-   All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
-   All of your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `js` extension

Required Files for the Project
------------------------------

### `package.json`

Click to show/hide file contents

### `.babelrc`

Click to show/hide file contents

### and...

Don't forget to run `$ npm install` when you have the `package.json`

Tasks
-----

### 0\. Install a redis instance

mandatory

Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - [https://redis.io/download/](https://alx-intranet.hbtn.io/rltoken/v6VB9ZwmVfppL0OmzbmVWQ "https://redis.io/download/")):

```
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make

```

-   Start Redis in the background with `src/redis-server`

```
$ src/redis-server &

```

-   Make sure that the server is working with a ping `src/redis-cli ping`

```
PONG

```

-   Using the Redis client again, set the value `School` for the key `Holberton`

```
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"

```

-   Kill the server with the process id of the redis-server (hint: use `ps` and `grep`)

```
$ kill [PID_OF_Redis_Server]

```

Copy the `dump.rdb` from the `redis-5.0.7` directory into the root of the Queuing project.

Requirements:

-   Running `get Holberton` in the client, should return `School`

**Repo:**

-   GitHub repository: `alx-backend`
-   Directory: `0x03-queuing_system_in_js`
-   File: `README.md, dump.rdb`

 Done? Help Get a sandbox

### 1\. Node Redis Client

mandatory

Install [node_redis](https://alx-intranet.hbtn.io/rltoken/mRftfl67BrNvl-RM5JQfUA "node_redis") using npm

Using Babel and ES6, write a script named `0-redis_client.js`. It should connect to the Redis server running on your machine:

-   It should log to the console the message `Redis client connected to the server` when the connection to Redis works correctly
-   It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work

**Requirements:**

-   To import the library, you need to use the keyword `import`

```
bob@dylan:~$ ps ax | grep redis-server
 2070 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$
bob@dylan:~$ npm run dev 0-redis_client.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
^C
bob@dylan:~$
bob@dylan:~$ ./src/redis-server > /dev/null 2>&1 &
[1] 2073
bob@dylan:~$ ps ax | grep redis-server
 2073 pts/0    Sl     0:00 ./src/redis-server *:6379
 2078 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$
bob@dylan:~$ npm run dev 0-redis_client.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client connected to the server
^C
bob@dylan:~$

```

**Repo:**

-   GitHub repository: `alx-backend`
-   Directory: `0x03-queuing_system_in_js`
-   File: `0-redis_client.js`

 Done? Help Get a sandbox

### 2\. Node Redis client and basic operations

mandatory

In a file `1-redis_op.js`, copy the code you previously wrote (`0-redis_client.js`).

Add two functions:

-   `setNewSchool`:
    -   It accepts two arguments `schoolName`, and `value`.
    -   It should set in Redis the value for the key `schoolName`
    -   It should display a confirmation message using `redis.print`
-   `displaySchoolValue`:
    -   It accepts one argument `schoolName`.
    -   It should log to the console the value for the key passed as argument

At the end of the file, call:

-   `displaySchoolValue('Holberton');`
-   `setNewSchool('HolbertonSanFrancisco', '100');`
-   `displaySchoolValue('HolbertonSanFrancisco');`

**Requirements:**

-   Use callbacks for any of the operation, we will look at async operations later

```
bob@dylan:~$ npm run dev 1-redis_op.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "1-redis_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 1-redis_op.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$

```

**Repo:**

-   GitHub repository: `alx-backend`
-   Directory: `0x03-queuing_system_in_js`
-   File: `1-redis_op.js`

 Done? Help Get a sandbox

### 3\. Node Redis client and async operations

mandatory

In a file `2-redis_op_async.js`, let's copy the code from the previous exercise (`1-redis_op.js`)

Using `promisify`, modify the function `displaySchoolValue` to use ES6 `async / await`

Same result as `1-redis_op.js`

```
bob@dylan:~$ npm run dev 2-redis_op_async.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "2-redis_op_async.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 2-redis_op_async.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$

```

**Repo:**

-   GitHub repository: `alx-backend`
-   Directory: `0x03-queuing_system_in_js`
-   File: `2-redis_op_async.js`

 Done? Help Get a sandbox

### 4\. Node Redis client and advanced operations

mandatory

In a file named `4-redis_advanced_op.js`, let's use the client to store a hash value

#### Create Hash:

Using `hset`, let's store the following:

-   The key of the hash should be `HolbertonSchools`
-   It should have a value for:
    -   `Portland=50`
    -   `Seattle=80`
    -   `New York=20`
    -   `Bogota=20`
    -   `Cali=40`
    -   `Paris=2`
-   Make sure you use `redis.print` for each `hset`

#### Display Hash:

Using `hgetall`, display the object stored in Redis. It should return the following:

**Requirements:**

-   Use callbacks for any of the operation, we will look at async operations later

```
bob@dylan:~$ npm run dev 4-redis_advanced_op.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "4-redis_advanced_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 4-redis_advanced_op.js`
Redis client connected to the server
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
{
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
}
^C
bob@dylan:~$

```

**Repo:**

-   GitHub repository: `alx-backend`
-   Directory: `0x03-queuing_system_in_js`
-   File: `4-redis_advanced_op.js`

 Done? Help Get a sandbox

### 5\. Node Redis client publisher and subscriber

mandatory

In a file named `5-subscriber.js`, create a redis client:

-   On connect, it should log the message `Redis client connected to the server`
-   On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`
-   It should subscribe to the channel `holberton school channel`
-   When it receives message on the channel `holberton school channel`, it should log the message to the console
-   When the message is `KILL_SERVER`, it should unsubscribe and quit

In a file named `5-publisher.js`, create a redis client:

-   On connect, it should log the message `Redis client connected to the server`
-   On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`
-   Write a function named `publishMessage`:
    -   It will take two arguments: `message` (string), and `time` (integer - in ms)
    -   After `time` millisecond:
        -   The function should log to the console `About to send MESSAGE`
        -   The function should publish to the channel `holberton school channel`, the message passed in argument after the time passed in arguments
-   At the end of the file, call:

```
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

```

**Requirements:**

-   You only need one Redis server to execute the program
-   You will need to have two node processes to run each script at the same time

**Terminal 1:**

```
bob@dylan:~$ npm run dev 5-subscriber.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "5-subscriber.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-subscriber.js`
Redis client connected to the server

```

**Terminal 2:**

```
bob@dylan:~$ npm run dev 5-publisher.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "5-publisher.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-publisher.js`
Redis client connected to the server
About to send Holberton Student #1 starts course
About to send Holberton Student #2 starts course
About to send KILL_SERVER
About to send Holberton Student #3 starts course
^C
bob@dylan:~$

```

**And in the same time in Terminal 1:**

```
Redis client connected to the server
Holberton Student #1 starts course
Holberton Student #2 starts course
KILL_SERVER
[nodemon] clean exit - waiting for changes before restart
^C
bob@dylan:~$

```

Now you have a basic Redis-based queuing system where you have a process to generate job and a second one to process it. These 2 processes can be in 2 different servers, which we also call "background workers".

**Repo:**

-   GitHub repository: `alx-backend`
-   Directory: `0x03-queuing_system_in_js`
-   File: `5-subscriber.js, 5-publisher.js`

 Done? Help Get a sandbox

### 6\. Create the Job creator

mandatory

In a file named `6-job_creator.js`:

-   Create a queue with `Kue`
-   Create an object containing the Job data with the following format:

```
{
  phoneNumber: string,
  message: string,
}

```

-   Create a queue named `push_notification_code`, and create a job with the object created before
-   When the job is created without error, log to the console `Notification job created: JOB ID`
-   When the job is completed, log to the console `Notification job completed`
-   When the job is failing, log to the console `Notification job failed`

```
bob@dylan:~$ npm run dev 6-job_creator.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 1

```

Nothing else will happen - to process the job, go to the next task!

If you execute multiple time this file, you will see the `JOB ID` increasing - it means you are storing new job to process...

**Repo:**

-   GitHub repository: `alx-backend`
-   Directory: `0x03-queuing_system_in_js`
-   File: `6-job_creator.js`

 Done? Help Get a sandbox

### 7\. Create the Job processor

mandatory

In a file named `6-job_processor.js`:

-   Create a queue with `Kue`
-   Create a function named `sendNotification`:
    -   It will take two arguments `phoneNumber` and `message`
    -   It will log to the console `Sending notification to PHONE_NUMBER, with message: MESSAGE`
-   Write the queue process that will listen to new jobs on `push_notification_code`:
    -   Every new job should call the `sendNotification` function with the phone number and the message contained within the job data

**Requirements:**

-   You only need one Redis server to execute the program
-   You will need to have two node processes to run each script at the same time
-   You muse use `Kue` to set up the queue

**Terminal 2:**

```
bob@dylan:~$ npm run dev 6-job_processor.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_processor.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_processor.js`
Sending notification to 4153518780, with message: This is the code to verify your account

```

**Terminal 1:** let's queue a new job!

```
bob@dylan:~$ npm run dev 6-job_creator.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 2

```

**And in the same time in Terminal 2:**

```
Sending notification to 4153518780, with message: This is the code to verify your account

```

BOOM! same as `5-subscriber.js` and `5-publisher.js` but with a module to manage jobs.

**Repo:**

-   GitHub repository: `alx-backend`
-   Directory: `0x03-queuing_system_in_js`
-   File: `6-job_processor.js`

 Done? Help Get a sandbox

### 8\. Track progress and errors with Kue: Create the Job creator

mandatory

In a file named `7-job_creator.js`:

Create an array `jobs` with the following data inside:

```
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

```

After this array created:

-   Create a queue with `Kue`
-   Write a loop that will go through the array `jobs` and for each object:
    -   Create a new job to the queue `push_notification_code_2` with the current object
    -   If there is no error, log to the console `Notification job created: JOB_ID`
    -   On the job completion, log to the console `Notification job JOB_ID completed`
    -   On the job failure, log to the console `Notification job JOB_ID failed: ERROR`
    -   On the job progress, log to the console `Notification job JOB_ID PERCENTAGE% complete`

**Terminal 1**:

```
bob@dylan:~$ npm run dev 7-job_creator.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "7-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_creator.js`
Notification job created: 39
Notification job created: 40
Notification job created: 41
Notification job created: 42
Notification job created: 43
Notification job created: 44
Notification job created: 45
Notification job created: 46
Notification job created: 47
Notification job created: 48
Notification job created: 49

```

**Repo:**

-   GitHub repository: `alx-backend`
