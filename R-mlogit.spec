%global packname  mlogit
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.2_2
Release:          1
Summary:          multinomial logit model
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-2.tar.gz
Requires:         R-Formula R-statmod R-lmtest R-maxLik R-zoo R-MASS 
Requires:         R-car R-nnet R-AER R-lattice 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Formula R-statmod R-lmtest R-maxLik R-zoo R-MASS
BuildRequires:    R-car R-nnet R-AER R-lattice 

%description
Estimation of the multinomial logit model

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
