%define dist MDV-Packdrakeng

# perl-Compress-Zlib is only "suggested"
%define __noautoreq 'perl\\(Compress::Zlib\\)'

Name:		perl-%{dist}
Version:	1.14
Release:	2
Summary:	Simple Archive Extractor/Builder
License:	GPLv2+
Group:		Development/Perl
Source0:	%{dist}-%{version}.tar.xz
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/rpm/MDV-Packdrakeng/
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl-JSON-PP
BuildRequires:	perl-devel
BuildArch:	noarch
Suggests:	perl(Compress::Zlib)

%description
MDV::Packdrakeng is a simple indexed archive builder and extractor using
standard compression methods.

%prep
%setup -q -n %{dist}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_mandir}/*/*
%{perl_vendorlib}/MDV/Packdrakeng
%{perl_vendorlib}/MDV/Packdrakeng.pm


%changelog
* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.13-9mdv2012.0
+ Revision: 763974
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.13-8
+ Revision: 763090
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.13-7
+ Revision: 667227
- mass rebuild

* Fri Jul 23 2010 Funda Wang <fwang@mandriva.org> 1.13-6mdv2011.0
+ Revision: 557109
- rebuild

* Sat Jan 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-5mdv2010.1
+ Revision: 485172
- fix build dependencies

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.13-4mdv2009.1
+ Revision: 351851
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.13-3mdv2009.0
+ Revision: 223819
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.13-2mdv2008.1
+ Revision: 180420
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 09 2007 Olivier Thauvin <nanardon@mandriva.org> 1.13-1mdv2008.0
+ Revision: 60786
- 1.13

* Mon Jun 18 2007 Pixel <pixel@mandriva.com> 1.12-1mdv2008.0
+ Revision: 40802
- new release, 1.12
- raise an exception when we can't write the generated .cz file
  (in case of "No space left on device")
- allow explicit call to $pack->DESTROY
  (to allow catching the exception above)

* Tue Jun 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.11-1mdv2008.0
+ Revision: 35317
- 1.11

* Thu May 17 2007 Olivier Thauvin <nanardon@mandriva.org> 1.10-1mdv2008.0
+ Revision: 27618
- 1.10

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.01-3mdv2008.0
+ Revision: 23364
- rebuild


* Wed Feb 15 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.01-2mdk
- Rebuild; use mkrel (misc)

* Fri Nov 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.01-1mdk
- 1.01

* Fri Oct 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.00-1mdk
- Initial MDV release

