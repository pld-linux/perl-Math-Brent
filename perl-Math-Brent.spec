%define		pdir	Math
%define		pnam	Brent
Summary:	Math::Brent - single dimensional function minimisation
Summary(pl.UTF-8):	Math::Brent - jednowymiarowa minimalizacja funkcji
Name:		perl-Math-Brent
Version:	0.01
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c3cf5b1a0715846387f77f8e3983df5f
Patch0:		%{name}-man.patch
URL:		http://search.cpan.org/dist/Math-Brent/
BuildRequires:	perl-Math-Fortran
BuildRequires:	perl-Math-VecStat
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Brent Perl module is an implementation of Brent's method for
One-Dimensional minimisation of a function without using derivatives.
This algorithm cleverly uses both the Golden Section Search and
parabolic interpolation.

%description -l pl.UTF-8
Moduł Perla Math::Brent stanowi implementację metody Brenta dla
jednowymiarowej minimalizacji funkcji bez korzystania z pochodnych.
Algorytm ten zręcznie korzysta zarówno ze znajdowania złotego
podziału, jak też z interpolacji kwadratowej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Brent.pm
%{_mandir}/man3/*
