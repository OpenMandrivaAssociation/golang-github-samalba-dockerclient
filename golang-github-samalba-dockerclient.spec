# http://github.com/samalba/dockerclient
%global goipath         github.com/samalba/dockerclient
%global commit          c37a52f55ab5a9edb9ffd4cf6e78692962b29b8d


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.11%{?dist}
Summary:        Docker client library in Go http://www.docker.com/
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

ExcludeArch: ppc64

%description
%{summary}

%package devel
Summary:       %{summary}

BuildRequires: golang(github.com/docker/docker/pkg/jsonlog)
BuildRequires: golang(github.com/docker/docker/pkg/stdcopy)
BuildRequires: golang(github.com/docker/docker/utils)
BuildRequires: golang(github.com/gorilla/mux)
BuildRequires: golang(github.com/stretchr/testify/mock)

%description devel
%{summary}

This package contains library source intended for
building other packages which use %{goipath}.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
# looks like this needs docker running
#.
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{goipath}/mockclient

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.gitc37a52f
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.gitc37a52f
- Polish spec and exclude ppc64
  related: #1212626

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitc37a52f
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitc37a52f
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitc37a52f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Apr 16 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitc37a52f
- First package for Fedora
  resolves: #1212626
