<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <xsl:output method="xml" indent="yes" />
  <xsl:strip-space elements="*" />
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()" />
    </xsl:copy>
  </xsl:template>
  <xsl:template match="//*[local-name()='FatturaElettronica']">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()" />
      <xsl:if test="not(*[local-name()='FatturaElettronicaHeader'])">
        <xsl:element name="FatturaElettronicaHeader" namespace="">
          <xsl:element name="CedentePrestatore" namespace="">
            <xsl:element name="IscrizioneREA" namespace="">
              <xsl:element name="Ufficio" namespace="">
                <xsl:text>TEST</xsl:text>
              </xsl:element>
            </xsl:element>
          </xsl:element>
        </xsl:element>
      </xsl:if>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="//*[local-name()='FatturaElettronica']/*[local-name()='FatturaElettronicaHeader']">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()" />
      <xsl:if test="not(*[local-name()='CedentePrestatore'])">
        <xsl:element name="CedentePrestatore" namespace="">
          <xsl:element name="IscrizioneREA" namespace="">
            <xsl:element name="Ufficio" namespace="">
              <xsl:text>TEST</xsl:text>
            </xsl:element>
          </xsl:element>
        </xsl:element>
      </xsl:if>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="//*[local-name()='FatturaElettronica']/*[local-name()='FatturaElettronicaHeader']/*[local-name()='CedentePrestatore']">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()" />
      <xsl:if test="not(*[local-name()='IscrizioneREA'])">
        <xsl:element name="IscrizioneREA" namespace="">
          <xsl:element name="Ufficio" namespace="">
            <xsl:text>TEST</xsl:text>
          </xsl:element>
        </xsl:element>
      </xsl:if>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="//*[local-name()='FatturaElettronica']/*[local-name()='FatturaElettronicaHeader']/*[local-name()='CedentePrestatore']/*[local-name()='IscrizioneREA']">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()" />
      <xsl:element name="Ufficio" namespace="">
        <xsl:text>TEST</xsl:text>
      </xsl:element>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>