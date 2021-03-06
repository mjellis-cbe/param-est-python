# Parameter Estimation (Python)

## Objective

- Approximate the rigorous kinetic model:

<img src="https://render.githubusercontent.com/render/math?math=r = \frac{ 71.82 \exp\left( \frac{7,867 }{ RT } \right) p^2_{ \textrm{CH}_3\textrm{OH} } }{ \left[1 %2B 3.9471 \times 10^{-4} \exp \left( \frac{37,835 }{RT} \right) p_{ \textrm{CH}_3\textrm{OH}  }^{1/2} %2B 5.6057 \times 10^{-6} \exp \left( \frac{47,468 }{ RT } \right) p_{ \textrm{H}_2\textrm{O} } \right]^4 }#gh-light-mode-only">
<img src="https://render.githubusercontent.com/render/math?math={\color{white}r = \frac{ 71.82 \exp\left( \frac{7,867 }{ RT } \right) p^2_{ \textrm{CH}_3\textrm{OH} } }{ \left[1 %2B 3.9471 \times 10^{-4} \exp \left( \frac{37,835 }{RT} \right) p_{ \textrm{CH}_3\textrm{OH}  }^{1/2} %2B 5.6057 \times 10^{-6} \exp \left( \frac{47,468 }{ RT } \right) p_{ \textrm{H}_2\textrm{O} } \right]^4 }}#gh-dark-mode-only">

with an approximate power law expression:

<img src="https://render.githubusercontent.com/render/math?math=\hat{r} = k_0 \exp\left( -\frac{E}{RT} \right) p_{\textrm{CH}_3\textrm{OH}}^{\alpha} p_{\textrm{H}_2\textrm{O}}^{\beta}#gh-light-mode-only">
<img src="https://render.githubusercontent.com/render/math?math={\color{white}\hat{r} = k_0 \exp\left( -\frac{E}{RT} \right) p_{\textrm{CH}_3\textrm{OH}}^{\alpha} p_{\textrm{H}_2\textrm{O}}^{\beta}}#gh-dark-mode-only">

## Method

- Use nonlinear least-squares
	1. Generate data from rigorous model
	1. Estimate the parameters that minimize the mean square error:

	<img src="https://render.githubusercontent.com/render/math?math=\underset{k_0, E_a, \alpha, \beta}{\textrm{minimize}} \frac{1}{N} \sum_{i=1}^N \left( \hat{r}(T_i, p_{ \textrm{CH}_3\textrm{OH},i }, p_{ \textrm{H}_2 \textrm{O},i}) - r(T_i, p_{ \textrm{CH}_3\textrm{OH},i}, p_{ \textrm{H}_2 \textrm{O},i}) \right)^2#gh-light-mode-only">
	<img src="https://render.githubusercontent.com/render/math?math={\color{white}\underset{k_0, E_a, \alpha, \beta}{\textrm{minimize}} \frac{1}{N} \sum_{i=1}^N \left( \hat{r}(T_i, p_{ \textrm{CH}_3\textrm{OH},i}, p_{ \textrm{H}_2 \textrm{O},i}) - r(T_i, p_{ \textrm{CH}_3\textrm{OH}, i }, p_{ \textrm{H}_2 \textrm{O} }) \right)^2}#gh-dark-mode-only">
