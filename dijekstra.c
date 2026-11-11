
#include <stdio.h>

#define INF 9999
#define MAX 10

int main()
{
    int cost[MAX][MAX], dist[MAX], visited[MAX];
    int n, i, j, src, count, min, next;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter cost adjacency matrix:\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &cost[i][j]);

    printf("Enter source vertex (0 to %d): ", n - 1);
    scanf("%d", &src);

    for (i = 0; i < n; i++)
    {
        dist[i] = cost[src][i];
        visited[i] = 0;
    }

    dist[src] = 0;
    visited[src] = 1;

    for (count = 1; count < n; count++)
    {
        min = INF;
        next = -1;

        for (i = 0; i < n; i++)
        {
            if (!visited[i] && dist[i] < min)
            {
                min = dist[i];
                next = i;
            }
        }

        if (next == -1)
            break;

        visited[next] = 1;

        for (i = 0; i < n; i++)
        {
            if (!visited[i] &&
                cost[next][i] < INF &&
                dist[next] + cost[next][i] < dist[i])
            {
                dist[i] = dist[next] + cost[next][i];
            }
        }
    }

    printf("\nShortest distances from vertex %d:\n", src);

    for (i = 0; i < n; i++)
    {
        if (dist[i] >= INF)
            printf("Vertex %d: Unreachable\n", i);
        else
            printf("Vertex %d: %d\n", i, dist[i]);
    }

    return 0;
}
