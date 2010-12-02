%define		pkgname	nagtail
Summary:	NagTail is like tail on the Nagios status logfile
Name:		nagios-%{pkgname}
Version:	0.0.31
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.vanheusden.com/nagtail/%{pkgname}-%{version}.tgz
# Source0-md5:	57bc082f9555c6736e5bc8c4d41fa4aa
Patch0:		default-statuslog.patch
URL:		http://www.vanheusden.com/nagtail/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NagTail is like tail on the Nagios status logfile.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%build
%{__make} nagtail \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	DEBUG="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags} -lstdc++"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p nagtail $RPM_BUILD_ROOT%{_bindir}
cp -a nagtail.1.gz $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/nagtail
%{_mandir}/man1/nagtail.1*
