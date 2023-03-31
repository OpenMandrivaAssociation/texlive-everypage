Name:		texlive-everypage
Version:	56694
Release:	2
Summary:	Provide hooks to be run on every page of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/everypage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides hooks to perform actions on every page, or
on the current page. Specifically, actions are performed after
the page is composed, but before it is shipped, so they can be
used to prepare the output page in tasks like putting
watermarks in the background, or in setting the next page
layout, etc.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/everypage
%doc %{_texmfdistdir}/doc/latex/everypage
#- source
%doc %{_texmfdistdir}/source/latex/everypage

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
