#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sub
%define	pnam	Usage
Summary:	Sub::Usage - issue subroutine/method usage
Summary(pl):	Sub::Usage - wy¶wietl informacje o sposobie u¿ycia funkcji/metody
Name:		perl-Sub-Usage
Version:	0.03
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a65e34e3500df80386a5316b43a7b671
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sub::Usage provides functions to display usage of subroutines or methods
from inside the stub.  Some people like to check the parameters of the
routine.

%description -l pl
Sub::Usage udostêpnia funkcje, wy¶wietlaj±ce informacje o sposobie u¿ycia
funkcji lub metody.  Niektórzy programi¶ci lubi± sprawdzaæ parametry
procedur.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README TODO
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*.3pm*
