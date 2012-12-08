%define upstream_name	 List-MoreUtils
%define upstream_version 0.32
# Fix circular build dependency:
# gprintify requires perl-List-MoreUtils
%define dont_gprintify 1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Provide the stuff missing in List::Util 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/List/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl-devel >= 2:5.14.2-1

%description
List::MoreUtils provides some trivial but commonly needed functionality on
lists which is not going to go into List::Util.

All of its functions are implementable in one line of Perl code. Using
the functions from this module however should give slightly better performance
as everything is implemented in C.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/List
%{perl_vendorarch}/auto/List
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.320.0-6
+ Revision: 765391
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.320.0-5
+ Revision: 763907
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.320.0-4
+ Revision: 762949
- rebuilt for new perl

* Thu Jan 19 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.320.0-3
+ Revision: 762808
- BuildRequires: perl >= 2:5.14.2 - the last build ended up being linked to 5.12 on x86_64

* Thu Jan 19 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.320.0-2
+ Revision: 762592
- Fix circular build dependency; build for perl 5.14.x

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.320.0-1
+ Revision: 677371
- update to new version 0.32

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.300.0-2
+ Revision: 667222
- mass rebuild

* Fri Dec 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.300.0-1mdv2011.0
+ Revision: 622699
- update to new version 0.30

* Wed Dec 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.290.0-1mdv2011.0
+ Revision: 616214
- update to new version 0.29

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.0-1mdv2011.0
+ Revision: 602030
- new version

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.250.0-5mdv2011.0
+ Revision: 564522
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-4mdv2011.0
+ Revision: 555263
- rebuild

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.250.0-3mdv2011.0
+ Revision: 555216
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

  + Funda Wang <fwang@mandriva.org>
    - New version 0.25

* Mon Jul 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2010.0
+ Revision: 400649
- update to 0.24
- using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.22-5mdv2009.0
+ Revision: 257640
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.22-4mdv2009.0
+ Revision: 245693
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.22-2mdv2008.1
+ Revision: 151326
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2008.0
+ Revision: 48621
- new version


* Tue Jun 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2007.0
- New version 0.21

* Mon Jun 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2007.0
- New release 0.20

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-2mdk
- fix buildrequires
- fix optimisations

* Fri Mar 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdk
- New release 0.19

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-2mdk
- fix sources URL
- conditional buildrequires

* Wed Mar 01 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.18-1mdk
- 0.18

* Tue Dec 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.17-1mdk
- 0.17

* Mon Nov 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.16-1mdk
- 0.16

* Wed Sep 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-1mdk
- 0.12

* Tue Sep 27 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.11-1mdk
- 0.11

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-2mdk 
- spec cleanup
- don't ship useless empty dirs
- make test in %%check

* Fri Apr 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.10-1mdk
- 0.10

* Tue Dec 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.09-1mdk 
- 0.09

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.06-1mdk
- 0.06

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.05-2mdk
- Rebuild for new perl

* Mon Oct 11 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.05-1mdk
- 0.05
- tweak description

* Sun Sep 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.04-1mdk 
- first mdk release

