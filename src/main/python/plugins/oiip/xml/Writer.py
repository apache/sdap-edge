import logging
import os
import os.path
import urllib.request, urllib.parse, urllib.error

from edge.writer.solrtemplateresponsewriter import SolrTemplateResponseWriter
from edge.response.solrjsontemplateresponse import SolrJsonTemplateResponse

class Writer(SolrTemplateResponseWriter):
    def __init__(self, configFilePath):
        super(Writer, self).__init__(configFilePath)

        templatePath = os.path.dirname(configFilePath) + os.sep
        templatePath += self._configuration.get('service', 'template')
        self.template = self._readTemplate(templatePath)

    def _generateOpenSearchResponse(self, solrResponse, searchText, searchUrl, searchParams, pretty):
        response = SolrJsonTemplateResponse()
        response.setTemplate(self.template)

        return response.generate(solrResponse, pretty=pretty)

    def _constructSolrQuery(self, startIndex, entriesPerPage, parameters, facets):
        queries = []

        for key, value in parameters.items():
            if value != "":
                if key == 'keyword':
                    queries.append(urllib.parse.quote(value))
                elif key == 'necessity':
                    queries.append("necessity:" + urllib.parse.quote(value))
                elif key == 'source':
                    queries.append("source_ss:\"" + urllib.parse.quote(value) + "\"")

        if len(queries) == 0:
            queries.append('*:*')

        query = 'q='+'+AND+'.join(queries)+'&version=2.2&indent=on&wt=json&start='+str(startIndex)+'&rows='+str(entriesPerPage)

        query += '&sort=category+asc'

        logging.debug('solr query: '+query)

        return query
