Name:		eayunstack-dashboard-theme
Version:	1.0
Release:	1%{?dist}
Summary:	EayunStack web user interface reference implementation theme module

License:	GPL
URL:		http://www.eayun.com
Source0:	eayunstack-dashboard-theme-1.0.tar.gz

BuildRequires:	/bin/bash
Requires:	openstack-dashboard

%description
EayunStack Dashboard branded logo.

%prep
%setup -q


%build


%install
mkdir -p %{buildroot}/usr/share/openstack-dashboard/static/dashboard/img/eayun/
tar -xzf img-replace.tgz -C %{buildroot}/usr/share/openstack-dashboard/static/dashboard/img/eayun/

%post
cp -f /usr/share/openstack-dashboard/static/dashboard/img/eayun/logo.png /usr/share/openstack-dashboard/static/dashboard/img/
cp -f /usr/share/openstack-dashboard/static/dashboard/img/eayun/logo-splash.png /usr/share/openstack-dashboard/static/dashboard/img/
cp -f /usr/share/openstack-dashboard/static/dashboard/img/eayun/favicon.ico /usr/share/openstack-dashboard/static/dashboard/img/
cp -f /usr/share/openstack-dashboard/static/dashboard/img/eayun/logo.png /usr/share/openstack-dashboard/openstack_dashboard/static/dashboard/img/
cp -f /usr/share/openstack-dashboard/static/dashboard/img/eayun/logo-splash.png /usr/share/openstack-dashboard/openstack_dashboard/static/dashboard/img/
cp -f /usr/share/openstack-dashboard/static/dashboard/img/eayun/favicon.ico /usr/share/openstack-dashboard/openstack_dashboard/static/dashboard/img/

%files
%doc
%attr(0644,root,root)/usr/share/openstack-dashboard/static/dashboard/img/eayun/logo.png
%attr(0644,root,root)/usr/share/openstack-dashboard/static/dashboard/img/eayun/logo-splash.png
%attr(0644,root,root)/usr/share/openstack-dashboard/static/dashboard/img/eayun/favicon.ico

%changelog

