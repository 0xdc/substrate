<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<div style="display:grid;grid-template-columns:6fr 2fr 1fr">
			<span style="border:solid">Filename</span>
			<span style="border:solid">Checksum (md5)</span>
			<span style="border:solid">Bytes</span>
			<xsl:for-each select="container/object">
				<span><a><xsl:attribute name="href" select="name"/><xsl:value-of select="name" /></a></span>
				<span style="font-family:monospace"><xsl:value-of select="hash" /></span>
				<span style="text-align:right"><xsl:value-of select="bytes" /></span>
			</xsl:for-each>
		</div>
	</xsl:template>

</xsl:stylesheet>
