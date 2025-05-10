#include <iostream>
using namespace std;

int main() {
    system("git add ."); // add all changes to the index
    string commit;
    cout << "Enter commit message: ";
    getline(cin, commit);
    string cmd = string("git commit -m \"") + commit + string("\"");
    system(cmd.c_str()); // execute the command in the terminal
    system("git branch -M main");
    system("git push -u origin main");
    return 0;
}