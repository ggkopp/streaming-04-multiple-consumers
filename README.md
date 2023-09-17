# streaming-04-multiple-consumers

## Author: Garrett Kopp 
## GitHub Repo: https://github.com/ggkopp/streaming-04-multiple-consumers

### Note: The following informaiton was performed in acending order. Responses to questions were answered post their completion. Each step is marked as "DONE" and all questions have been answered and images provided where requested. Thanks for reading! 

> Use RabbitMQ to distribute tasks to multiple workers

One process will create task messages. Multiple worker processes will share the work. 


## Before You Begin - DONE

1. Fork this starter repo into your GitHub.
1. Clone your repo down to your machine.
1. View / Command Palette - then Python: Select Interpreter
1. Select your conda environment. 

## Read - DONE

1. Read the [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
1. Read the code and comments in this repo.

## RabbitMQ Admin - DONE

RabbitMQ comes with an admin panel. When you run the task emitter, reply y to open it. 

(Python makes it easy to open a web page - see the code to learn how.)

## Execute the Producer - DONE 

1. Run emitter_of_tasks.py (say y to monitor RabbitMQ queues)

Explore the RabbitMQ website.

## Execute a Consumer / Worker - DONE

1. Run listening_worker.py

Will it terminate on its own? How do you know? It will not terminate independently. You have to use the Ctrl+C to exit the listening. 

## Ready for Work - DONE

1. Use your emitter_of_tasks to produce more task messages.

## Start Another Listening Worker - DONE

1. Use your listening_worker.py script to launch a second worker. 

Follow the tutorial. 
Add multiple tasks (e.g. First message, Second message, etc.)
How are tasks distributed? It seems that the terminals share the load. One will recieve one, then the other file will take the next, and this will go on over and over. Every other send goes to one worker. 
Monitor the windows with at least two workers. 
Which worker gets which tasks? One worker gets the even sends, the other gets the odd sends. When one is busy the other takes the job. 


## Reference

- [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)


## Screenshot - DONE

See a running example with at least 3 concurrent process windows here:

In these shots you can see the workers taking the even or odd messages that are emitted from the tasks emitted. Also, you can see the RabbitMQ's response to the sends. It show the RabbitMQ UI queueing the messages in the event there is there is not workers available. 

![Alt text](<Multiple Terminal 1.png>)

![Alt text](<Multiple Terminal 2.png>)