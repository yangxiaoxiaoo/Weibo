#include <iostream>
#include <dirent.h>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
#define USERNUM 1300
#define COMNUM 100
//long int dict[1300000][3700];
//user file in directory BigCommenterHashed = 1201937, every user maximun comments
//biggest file 123682651 has line number = 3611

//list all files in current directory passed as argument in STL vector
//open gives a vector of files
std::vector<std::string> open(std::string path = "."){
    DIR* dir;
    dirent* pdir;
    std::vector<std::string> files;
    
    dir = opendir(path.c_str());
    while ((pdir = readdir(dir))) {
        files.push_back(pdir->d_name);
    }
    std::cout << "number of files read:======="<< files.size();
    return files;
}

//calculate the jaccard of user1 and user2
float jaccard(long int* user1 , long int* user2, int len1, int len2)
{
    std::vector<long int> v1(len1+len2);
    std::vector<long int> v2(len1+len2);

    std::vector<long int>::iterator it1;
    std::vector<long int>::iterator it2;

    std::sort(user1, user1+len1);
    std::sort(user2, user2+len2);
    
    it1 = std::set_intersection (user1, user1+len1, user2, user2+len2, v1.begin());
    it2 = std::set_union (user1, user1+len1, user2, user2+len2, v2.begin());

    v1.resize(it1-v1.begin());
    v2.resize(it2-v2.begin());
    
    float rate = float(v1.size()) / float(v2.size());
    return rate;
    
}

int main()
{
    std::string line;
    long int int_line;

    long int dict[USERNUM][COMNUM];
    int lenth[USERNUM];
    std::vector<std::string> f;
    f = open();
    std::fstream file;
    int i;
    for (i = 0; i<f.size(); i++) {
        std::cout << f[i] << '\n';
        //long int* array of file i's all comments
        
        
        //iterate other file name except for script files
        if ((f[i] != "Comp_jaccard.cpp") && (f[i] != "Comp")) {
            const char* pass_str = f[i].c_str();
            std::ifstream infile(pass_str);
            //g++ on achtung read not ifstream
            if (infile.is_open())
            {
                //std::cout << "---head if a file---";
                int line_index = -1;
                while (infile.good()) {
                    getline (infile, line);
                    line_index ++;
                    //std::cout << "-size of this line is" << line.size();
                    //size of line should be 32--an MD5 hashed integer
                    if (1) {
                        try {
                            //avoid overflow, we dont mind occasional collision
                            const char* char_line = line.substr(1,10).c_str();
                            int_line = strtol(char_line,NULL,16);
                            //std::cout << int_line << '\n';
                            dict[i][line_index] = int_line;
                        } catch (...) {
                            std::cout << "stoi converting error!" << line;
                        }
                    }
                    //in while end, line_index record the line number
                    lenth[i] = line_index;
                }
            }
            else std::cout << "read file error" << i;
        }
        else std::cout << "script files...=.=";
        
    }//end of for all file read dictionary
    std::cout << "end of initializing dixtionary"<<'\n';
    
    //for all filename = username = f[i], calculate its jaccard to user f[j]
    //write jaccard index into file "jaccard.txt"
    float jaccard_index;
    int j = 0;
    std::ofstream outfile;
    outfile.open ("jaccard.txt");
    for (i = 0; i<f.size(); i++) {
        for (j = 0; j<f.size(); j++) {
            jaccard_index = jaccard(dict[i], dict[j], lenth[i], lenth[j]);
            //batch write to file to save time cant fit into memory
            outfile << f[i] << ' ' << f[j] << ' '<< jaccard_index << '\n';
        }
    }
    outfile.close();
    
    return 0;
}

