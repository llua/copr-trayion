Name:               trayion
Version:            1.2
Release:            1
Summary:            Ion3/Notion friendly systray
Source:             https://github.com/laynor/%{name}/archive/%{version}.tar.gz
URL:                https://github.com/laynor/trayion
Group:              System/GUI/Other
License:            GNU General Public License version 2
BuildRequires:      gcc
BuildRequires:      libX11-devel

%description
Ion3/Notion friendly systray, featuring configurable icon hiding and sorting


%prep
%setup -q -n %{name}-%{version}

%build
%__make %{?_smp_flags} \
    prefix="%{_prefix}"

%install
%__make \
    prefix="%{buildroot}/usr" \
    install

%clean
%__rm -rf %{buildroot}

%files
/usr/bin/trayion
/usr/share/man/man1/trayion.1.gz


%changelog
* Sun Sep 08 2019 Eric Cook <llua@gmx.com> - 1.2
- initial version
