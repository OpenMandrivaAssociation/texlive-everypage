Name:		texlive-everypage
Version:	1.1
Release:	1
Summary:	Provide hooks to be run on every page of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/everypage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides hooks to perform actions on every page, or
on the current page. Specifically, actions are performed after
the page is composed, but before it is shipped, so they can be
used to prepare the output page in tasks like putting
watermarks in the background, or in setting the next page
layout, etc.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/everypage/everypage.sty
%doc %{_texmfdistdir}/doc/latex/everypage/README
%doc %{_texmfdistdir}/doc/latex/everypage/everypage.pdf
#- source
%doc %{_texmfdistdir}/source/latex/everypage/everypage.dtx
%doc %{_texmfdistdir}/source/latex/everypage/everypage.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
