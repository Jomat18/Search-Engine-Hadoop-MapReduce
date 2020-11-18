#include <string.h>
#include <stdio.h> 
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <time.h> 

using namespace std;

int main() {
	long int iterations = 2000; //Cantida de texto
	int size;

    char str[] = "In computer science a trie also called digital tree or prefix tree is a kind of search tree an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings Unlike a binary search tree no node in the tree stores the key associated with that node instead its position in the tree defines the key with which it is associated ie the value of the key is distributed across the structure All the descendants of a node have a common prefix of the string associated with that node and the root is associated with the empty string Keys tend to be associated with leaves though some inner nodes may correspond to keys of interest Hence keys are not necessarily associated with every node For the space optimized presentation of prefix tree see compact prefix tree Copyright laws are changing all over the world be sure to check the copyright laws for your country before posting these files Please take a look at the important information in this header We encourage you to keep this file on your own disk keeping an electronic path open for the next readers Do not remove this While the family were in this confusion Charlotte Lucas came to spend the day with them She was met in the vestibule by Lydia Although IT security and information security sound similar they do refer to different types of security Information security refers to the processes and tools designed to protect sensitive business information from invasion whereas IT security refers to securing digital data through computer network security Network security is used to prevent unauthorized or malicious users from getting inside your network This ensures that usability reliability and integrity are uncompromised This type of security is necessary to prevent a hacker from accessing data inside the network It also prevents them from negatively affecting your users ability to access or use the network Wildlife fans will delight in these exceptional documentaries about the wonders of the animal kingdom Kids will love getting to see their favorite animals up close and personal from tiny insects to gigantic elephants Keep in mind some of these documentaries focus on predators on the hunt and others show the brutal conditions faced by creatures in captivity So make sure you know what your kids can handle before diving into a documentary like Blackfish To learn more about the environment and what we can do to protect it check out our list of Green"; 
    
    vector<string> input;
    
    char *token = strtok(str, " "); 

    while (token != NULL) 
    { 
        input.push_back(token); 
        token = strtok(NULL, " "); 
    } 
    
    size = input.size();

    for (int n=0; n<100; n++) { //Nro de archivos

    	ofstream outfile;

      	outfile.open("static/corpus/file_"+to_string(n)+".txt", ios_base::app); 

        srand (time(NULL));

        for (int i=0; i<iterations; i++) 
        	outfile << input[rand()%size]<<" ";

        outfile.close();
    }

	return 0;
}
