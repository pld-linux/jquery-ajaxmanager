# TODO
# - paths and deps for demo
%define		plugin	ajaxmanager
Summary:	jQuery AJAX Queue/Cache/Abort/Block Manager
Name:		jquery-%{plugin}
Version:	3.12
Release:	1
License:	MIT / GPL v2
Group:		Applications/WWW
Source0:	https://github.com/aFarkas/Ajaxmanager/tarball/%{version}/%{name}-%{version}.tgz
# Source0-md5:	3ea0c90115bb3b949647c3bd111de115
URL:		https://github.com/aFarkas/Ajaxmanager
BuildRequires:	closure-compiler
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	yuicompressor
Requires:	jquery >= 1.2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
An jQuery Plugin, wich helps you to manage AJAX requests and responses
(i.e. abort requests, block requests, order requests).

%package demo
Summary:	Demo for jQuery.ajaxmanager
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.ajaxmanager
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.ajaxmanager.

%prep
%setup -qc
mv *-Ajaxmanager-*/* .

%build
install -d build/css

# compress .js
js=jquery.%{plugin}.js
out=build/$js
%if 0%{!?debug:1}
closure-compiler --js $js --charset UTF-8 --js_output_file $out
js -C -f $out
%else
cp -p $js $out
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p build/jquery.%{plugin}.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a index.html $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
