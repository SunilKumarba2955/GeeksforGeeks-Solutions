//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	
	public:
	vector<int> downwardDiagonal(int n, vector<vector<int>> a)
	{
	    vector<int> v;
		int i=0,j=0;
        while(i<n)
        {
           i=0;
           while(j>=0)
           {
               v.push_back(a[i++][j--]);
           }
           j=i;
        }
        i=1;
        while(i<n)
        {
           j=n-1;
           while(i<n)
           {
               v.push_back(a[i++][j--]);
           }
           i=j+2;
        }
        return v;
	}
};


//{ Driver Code Starts.



int main()
{

    
    int t;
    cin >> t;
    while(t--) 
    {
        int n;
        cin >> n;

        vector<vector<int>> A(n, vector<int>(n));

        for(int i = 0; i < n; i++)
        	for(int j = 0; j < n; j++)
        		cin >> A[i][j];

        Solution obj;
        vector<int> ans = obj.downwardDiagonal(n, A);

        for(auto i:ans)
        	cout << i << " ";

	    cout << "\n";
    }

    return 0;
}

// } Driver Code Ends