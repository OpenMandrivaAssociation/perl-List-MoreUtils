%define module	List-MoreUtils
%define name	perl-%{module}
%define version 0.22
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Provide the stuff missing in List::Util 
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/List/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
List::MoreUtils provides some trivial but commonly needed functionality on
lists which is not going to go into List::Util.

All of its functions are implementable in one line of Perl code. Using
the functions from this module however should give slightly better performance
as everything is implemented in C.

%prep
%setup -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%__make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/List
%{perl_vendorarch}/auto/List
%{_mandir}/*/*

