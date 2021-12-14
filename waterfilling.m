function [Pn_opt,mu] = waterfilling(csi,P_total)
% csi will be a vector of size 1*n
% P_total is a positive quantity

n = length(csi); % number of parallel channels
M = 1e4;
mu_axis = linspace(1e-15,5,M);

Pn = max(1./mu_axis - (1./csi)',0);
g = sum(log2(1 + Pn.* (repmat(csi',[1 M])))) - ...
    mu_axis.*(sum(Pn) - P_total); % Dual equation
[ming,ind] = find(g == min(g));

mu = mu_axis(ind); % The power level 

Pn_opt = max(1/mu - 1./csi,0);

f1 = figure(1);
clf(f1);
plot(mu_axis,g);
grid on;

f2 = figure(2);
clf(f2);
subplot(2,1,1);
set(f2,'Color',[1 1 1]);
bar(Pn_opt,1,'r');
subplot(2,1,2)
set(f2,'Color',[1 1 1]);
bar(csi,1,'b');

end


