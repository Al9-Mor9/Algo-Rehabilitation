import java.io.*;
import java.util.*;

class Node{
	int leaf, weight;
	public Node(int leaf, int weight) {
		this.leaf = leaf;
		this.weight = weight;
	}
}

public class 1967_L {
	static int n;
	static ArrayList<Node> lst[];
	static boolean visit[];
	static int ans = 0;
	public static void main(String[] args) throws Exception {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	    n = Integer.parseInt(br.readLine());
	    lst = new ArrayList[n + 1];

	    for(int i = 1; i <=n ; i++)  lst[i] = new ArrayList<Node>();
	    for(int i=1; i<=n-1; i++) {
	    	StringTokenizer st = new StringTokenizer(br.readLine());
	    	int p = Integer.parseInt(st.nextToken());
	    	int c = Integer.parseInt(st.nextToken());
	    	int w = Integer.parseInt(st.nextToken());
	    	lst[p].add(new Node(c, w));
	    	lst[c].add(new Node(p, w));
	    }

	    for(int i = 1; i <= n; i++) {
	    	visit = new boolean[n + 1];
	    	visit[i] = true;
	    	dfs(i, 0);
	    }
	    bw.write(String.valueOf(ans));
	    bw.flush();
	    bw.close();
	    br.close();
	    }

    static void dfs(int start, int s) {
        if (n == 1) return;
        ans = Math.max(s, ans);
        
        for(int i = 0; i < lst[start].size(); i++) {
            int tmp = lst[start].get(i).leaf;

            if(visit[tmp]) continue;
            visit[tmp] = true;
            dfs(tmp, lst[start].get(i).weight + s);
            visit[tmp] = false;
        }
    }
}

