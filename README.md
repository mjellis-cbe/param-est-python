# Parameter Estimation (Python)

## Objective

- Approximate the rigorous kinetic model:
<img src="https://render.githubusercontent.com/render/math?math=r = \frac{ 71.82 \exp\left( \frac{ + 7,867 }{ RT } \right) p^2_{ \textrm{CH}_3\textrm{OH} } }{ \left[ 1 + 3.9471 \times 10^{-4} \exp \left( \frac{ + 37,835 }{RT} \right) p_{ \textrm{CH}_3\textrm{OH}  }^{1/2} + 5.6057 \times 10^{-6} \exp \left( \frac{ + 47,468 }{ RT } \right) p_{ \textrm{H}_2\textrm{O} } \right]^4 }">

with an approximate power law expression:
<img src="https://render.githubusercontent.com/render/math?math=\hat{r} = k_0 \exp\left( -\frac{E}{RT} \right) p_{\textrm{CH}_3\textrm{OH}}^{\alpha} p_{\textrm{H}_2\textrm{O}}^{\beta}">

## Method

- Use nonlinear least-squares
	1. Generate data from rigorous model
	1. Estimate the parameters that minimize the mean square error:
	<img src="https://render.githubusercontent.com/render/math?math=\underset{}{\textrm{minimize}} ~\frac{1}{N} \sum_{i=1}^N \left( r(T_i, p_{ \textrm{CH}_3\textrm{OH}, i }, p_{ \textrm{H}_2 \textrm{O} }) - \hat{r}(T_i, p_{ \textrm{CH}_3\textrm{OH}, i }, p_{ \textrm{H}_2 \textrm{O} }) \right)^2">
