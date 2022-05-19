let url;

if (process.env.NODE_ENV === 'development') url = 'http://localhost:3000';
else url = 'http://some.production.url:3000';

export default url;