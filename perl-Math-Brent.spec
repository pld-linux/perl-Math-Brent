%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Brent
Summary:	Math::Brent perl module
Summary(pl):	Modu� perla Math::Brent
Name:		perl-Math-Brent
Version:	0.01
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Math-Fortran
BuildRequires:	perl-Math-VecStat
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Brent - Single Dimensional Function Minimisation.

%description -l pl
Modu� perla Math::Brent.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Math/Brent.pm
%{_mandir}/man3/*
