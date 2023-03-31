Name:		texlive-mathlig
Version:	54244
Release:	2
Summary:	Define maths "ligatures"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathlig
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathlig.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines character sequences that "behave like"
ligatures, in maths mode. Example definitions (chosen to show
the package's flexibility, are: \mathlig{->}{\rightarrow}
\mathlig{<-}{\leftarrow} \mathlig{<->}{\leftrightarrow}

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/mathlig

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
