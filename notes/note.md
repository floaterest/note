% Notes


```
S -> e, 0, 1
S -> 1S1, 0S0, 0S1, 1S0
```

$$\usetikzlibrary{automata}\tikzset{initial text=}\begin{tikzpicture}[scale=2]
    \node[state,initial]at(0,0)(l){$w$};
    \node[state,accepting]at(2,0)(r){$w^R$};
    \path[->]
        (r)edge[loop above] node[above]{\begin{tabular}{c}
            $1:1\to\epsilon$\\
            $0:0\to\epsilon$\\
        \end{tabular}}()
        (l)edge[loop above] node[above]{\begin{tabular}{c}
            $1:\epsilon\to1$\\
            $0:\epsilon\to0$\\
        \end{tabular}}()
           edge node[above]{\begin{tabular}{c}
            $\epsilon:\epsilon\to\epsilon$\\
            $0:\epsilon\to\epsilon$\\
            $1:\epsilon\to\epsilon$\\
        \end{tabular}}(r);
\end{tikzpicture}$$

