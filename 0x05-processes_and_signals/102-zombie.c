#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop
 *
 * Return: Always returns 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point of the program
 *
 * Return: Always returns 0
 */
int main(void)
{
	pid_t zombie_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid == 0)
		{
			exit(0); /* Child process exits immediately, becoming a zombie */
		}
		else if (zombie_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", zombie_pid);
			sleep(1); /* Wait for a moment before creating the next zombie */
		}
		else
		{
			perror("fork");
		}
	}

	infinite_while(); /* Parent process enters an infinite loop */
	return (0);
}
