%global tl_name everypage
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0b
Release:	%{tl_revision}.1
Summary:	Provide hooks to be run on every page of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/everypage
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides hooks to perform actions on every page, or on the
current page. Specifically, actions are performed after the page is
composed, but before it is shipped, so they can be used to prepare the
output page in tasks like putting watermarks in the background, or in
setting the next page layout, etc.

