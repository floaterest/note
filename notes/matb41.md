% MATB41 Post-Midterm



# 03 Higher-Order Derivatives

<details class="definition" open><summary>$f$ of class $C^n$</summary>
$f$ is class $C^n$ 

- iff $f$ is $n$ times continuously diffable 
- iff all $n$th derivative of $f$ is continuous

i.e. e.g. $\displaystyle\frac{\partial^2f}{\partial x^2}=\frac\partial{\partial x}\left(\frac{\partial f}{\partial x}\right)$ is continuous
</details>
<details class="theorem" open><summary>Mixed Partials</summary>
if $f:\R^2\to\R$ is class $C^2$ then
$$\frac{\partial^2f}{\partial x\partial y}=\frac{\partial^2f}{\partial y\partial x}$$
</details>
<details class="example" open><summary>given $z=f(x,y)$ find $\dfrac{\partial^2z}{\partial r^2}$ as polar coordinate</summary>
given $x=r\cos\theta$ and $y=r\sin\theta$

::: {style="font-size: 90%"}

$$\begin{align*}
\therefore\frac{\partial z}{\partial r}&=\nabla f\cdot\begin{pmatrix}\dfrac{\partial x}{\partial r}&\dfrac{\partial y}{\partial r}\end{pmatrix}=\frac{\partial z}{\partial x}\cos\theta+\frac{\partial z}{\partial y}\sin\theta\\
\therefore\frac{\partial^2z}{\partial r^2}&=\frac\partial{\partial r}\left(\frac{\partial z}{\partial r}\right)=\frac\partial{\partial r}\left(\frac{\partial z}{\partial x}\right)\cos\theta+\frac\partial{\partial r}\left(\frac{\partial z}{\partial y}\right)\sin\theta\\
\because\frac\partial{\partial r}\left(\frac{\partial z}{\partial x}\right)&=\nabla\left(\frac{\partial z}{\partial x}\right)\cdot\begin{pmatrix}\dfrac{\partial x}{\partial r}&\dfrac{\partial y}{\partial r}\end{pmatrix}=\begin{pmatrix}\dfrac{\partial z}{\partial x^2}&\dfrac{\partial z}{\partial x\partial y}\end{pmatrix}\cdot\begin{pmatrix}\dfrac{\partial x}{\partial r}&\dfrac{\partial y}{\partial r}\end{pmatrix}\\
&=\frac{\partial z}{\partial x^2}\cos\theta+\frac{\partial z}{\partial x\partial y}\sin\theta\\
\end{align*}$$

:::
</details>
