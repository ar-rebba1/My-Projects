// diceApp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>
using namespace std;
int numPlayers;
vector <string> players;
string userInput;
string playerName;
int main()
{
	srand(time(NULL));
	cout << "Enter a number of cards: ";
	cin >> numPlayers;
	cout << endl;
	cout << "Number of players: " << numPlayers << endl;
	for (int i = 0; i < numPlayers; i++) {
		cout << "Player "<< i+1 << ": " << endl;
		cin >> playerName;
		players.push_back(playerName);
		//cout << "Current player:" << players.at(i) << endl;
	}
	while (true) {
		for (auto j = players.begin(); j != players.end(); ++j) {
			cout << "Type in 'roll' to roll the dice or 'stop' to end the game: ";
			cin >> userInput;
			cout << endl;
			if (userInput == "roll") {
				cout << *j << "'s turn" << endl;
				cout << "Rolling..." << endl;
				cout << "Result: " << (rand() % 6) + 1 << endl;
			}
			else if (userInput == "stop")
			{
				cout << "Good game";
				exit(0);
			}
			else {
				cout << "Enter a valid response" << endl;
				--j;
			}
			if (j == players.end()) {
				continue;
			}
		}
	}
}

